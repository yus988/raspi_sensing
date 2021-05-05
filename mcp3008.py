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

def main():
    spi = spidev.SpiDev()
    # spi.open(bus,device)
    spi.open(0, 0)
    spi.max_speed_hz = 1000000

    spi2 = spidev.SpiDev()
    # spi.open(bus,device)
    spi2.open(0, 1)
    spi2.max_speed_hz = 1000000

    # 書き込むファイルの作成
    dt_now = datetime.datetime.now()
    filename = './csv/' + dt_now.strftime('%m-%d_%H-%M-%S') + '.csv'
    print(dt_now.strftime('%m%d_%H-%M-%S'))

    # ファイルオープン
    f = open(filename, 'w')
    writer = csv.writer(f, lineterminator='\n')
    csvlist = []

    # tmp 配列
    data = []
    volts = []
    # 1ch -> 0, ..., 8ch -> 7
    
    vref = 5.0 # MCP3008 の Vref に入れた電圧. ここでは 5V
    try:
        while True:
            # print(perf_counter())

            for i in range(9):
                if i < 8 :
                    data = readAdc(i, spi)
                else :
                    channel = i - 8
                    data = readAdc(channel, spi2)
                volts = convertVolts(data, vref)
                csvlist.append([perf_counter(), volts, i])
                print(volts,i)
            # MCP3008 の Vref に入れた電圧. ここでは 5V
            # time.sleep(1)

    except KeyboardInterrupt:
        writer.writerows(csvlist)
        f.close()
        print('!FINISH!')

if __name__ == "__main__":
    main()