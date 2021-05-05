#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter
import csv
import datetime
import random
import tkinter as tk

isRecord = False
count = 0
tmpArr = []

# main recoding program


def recording():
    global app, isRecord, label
    if isRecord:
        # print(perf_counter())
        for i in range(6):
            # tmpArr[i] = random.random()
            # print(tmpArr[i])
            print(perf_counter())
        app.after(0, recording)


# triggerd by btnStart
def toggleRecord(event):
    global app, isRecord, label, toggleBtn
    if not isRecord:
        isRecord = True
        # toggleBtn['text']="Recording"
        btnText.set("Recording...")
        toggleBtn.configure(bg='pale green')
        app.after(100, recording)
    else:
        isRecord = False
        # toggleBtn['text']="Start recording"
        app.quit()
        # btnText.set("Start recording")
        # toggleBtn.configure(bg='white')


app = tk.Tk()
app.title("hoge")
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
btnText.set("Start recording")
# creating start buttun
toggleBtn = tk.Button(
    app,
    textvariable=btnText,
    height=360,
    width=240)

toggleBtn.pack()
toggleBtn.bind("<ButtonPress>", toggleRecord)



app.mainloop()

# def main():
#     # 書き込むファイルの作成
#     dt_now = datetime.datetime.now()
#     filename = './csv/' + dt_now.strftime('%m-%d_%H-%M-%S') + '.csv'
#     print(dt_now.strftime('%m%d_%H-%M-%S'))

#     # ファイルオープン
#     f = open(filename, 'w')
#     writer = csv.writer(f, lineterminator='\n')
#     csvlist = []

#     # tmp 配列
#     data = []
#     volts = []
#     # 1ch -> 0, ..., 8ch -> 7

#     vref = 5.0 # MCP3008 の Vref に入れた電圧. ここでは 5V
#     try:
#         while True:
#             # print(perf_counter())

#             for i in range(6):
#                 data = readAdc(i, spi)
#                 volts = convertVolts(data, vref)
#                 csvlist.append([perf_counter(), volts, i])

#             print(volts)
#             # MCP3008 の Vref に入れた電圧. ここでは 5V
#             # time.sleep(1)

#     except KeyboardInterrupt:
#         writer.writerows(csvlist)
#         f.close()
#         print('!FINISH!')
