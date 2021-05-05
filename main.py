#!/usr/bin/env python
# -*- coding:utf-8 -*-
import spidev
import time
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter
import csv
import datetime
import tkinter as tk

isRecord = False
count = 0

spi = spidev.SpiDev()
# spi.open(bus,device)
spi.open(0, 0)
spi.max_speed_hz = 1000000
vref = 5.0 # MCP3008 の Vref に入れた電圧. ここでは 5V

# 1ch -> 0, ..., 8ch -> 7
csvlist = []
dt_now = datetime.datetime.now()
filename = './csv/' + 'init' + '.csv'
# ファイルオープン
f = open(filename, 'w')
writer = csv.writer(f, lineterminator='\n')


# 解説参照
def readAdc(channel, spi):
    adc = spi.xfer2([1, (8 + channel) << 4, 200])
    # print(adc)
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def convertVolts(data, vref):
    volts = (data * vref) / float(1023)
    volts = round(volts, 4)
    return volts

def recording():
    global app, isRecord, label
    global f,writer,csvlist
    if isRecord:
        # print(perf_counter())
        for i in range(6):
            data = readAdc(i, spi)
            volts = convertVolts(data, vref)
            csvlist.append([perf_counter(), volts, i])
            print(volts)
        app.after(0, recording)

# triggerd by btnStart
def toggleRecord(event):
    global app, isRecord, label, toggleBtn
    global f,writer,csvlist,dt_now
    if not isRecord:
        isRecord = True
        btnText.set("Recording...")
        toggleBtn.configure(bg='pale green')
        initWriter()
        app.after(1000, recording)

    else: # stop recording and save the data
        isRecord = False
        writer.writerows(csvlist)
        f.close()
        print('!FINISH!', dt_now)
        # toggleBtn['text']="Start recording"
        btnText.set("Start \n Recording")
        toggleBtn.configure(bg='white')

def initWriter():
    global f,writer,csvlist,dt_now
    f.close()
    # 書き込むファイルの作成
    dt_now = datetime.datetime.now()
    filename = './csv/' + dt_now.strftime('%m-%d_%H-%M-%S') + '.csv'
    print(dt_now.strftime('%m%d_%H-%M-%S'))
    # ファイルオープン
    f = open(filename, 'w')
    writer = csv.writer(f, lineterminator='\n')
    csvlist = []

app = tk.Tk()
app.title("ADC recorder")
app.geometry("360x240")
# create label
label = tk.Label(
    app,
    width=10,
    height=1,
    text=0,
    font=("", 20)
)
# label.pack()

btnText = tk.StringVar()
btnText.set("Start \n Recording")
# creating start buttun
toggleBtn = tk.Button(
    app,
    textvariable=btnText,
    height=360,
    width=240,
    font=("", 40),
    )

toggleBtn.pack()
toggleBtn.bind("<ButtonPress>", toggleRecord)


app.mainloop()


