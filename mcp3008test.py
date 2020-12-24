#!/usr/bin/env python
# -*- coding:utf-8 -*-
import spidev
import time
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter
import csv
import datetime


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


    # 書き込むファイルの作成
    dt_now = datetime.datetime.now()
    filename = './csv/' + dt_now.strftime('%m-%d_%H-%M-%S') + '.csv'
    print(dt_now.strftime('%m%d_%H-%M-%S'))

    # # ファイルオープン
    f = open(filename, 'w')
    writer = csv.writer(f, lineterminator='\n')
    csvlist = []

    fig, ax = plt.subplots(1, 1)
    x = np.arange(0, 100, 1)
    y = np.zeros(100)
    lines, = ax.plot(x, y)
    data = []
    volts = []
    # 1ch -> 0, ..., 8ch -> 7
    ch = 2
    v = 5.0
    try:

        while True:
            # print(perf_counter())

            for i in range(1):
                data = readAdc(i, spi)
                volts = convertVolts(data, v)
                csvlist.append([perf_counter(), i, volts])

            print(volts)
            # MCP3008 の Vref に入れた電圧. ここでは 5V
            # x += 1
            # y = np.append(y, vpolts)
            # y = np.delete(y, 0)
            # # print(y)
            # lines.set_data(x, y)
            # ax.set_xlim((x.min(), x.max()))
            # ax.set_ylim((y.min(), y.max()))
            # plt.pause(.001)

    except KeyboardInterrupt:
        writer.writerows(csvlist)
        f.close()
        print('!FINISH!')


if __name__ == "__main__":
    main()
