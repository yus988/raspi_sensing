#!/usr/bin/env python
# -*- coding:utf-8 -*-
import spidev
import time

# 解説参照
def readAdc(channel,spi):
    adc = spi.xfer2([1, (8 + channel) << 4, 200])
    print(adc)
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def convertVolts(data, vref):
    volts = (data * vref) / float(1023)
    volts = round(volts,4)
    return volts


def main():
    spi = spidev.SpiDev()
    # spi.open(bus,device)
    spi.open(0,0)
    spi.max_speed_hz = 1000000
    # 1ch -> 0, ..., 8ch -> 7
    ch = 0
    while True: 
        data = readAdc(ch,spi)
        # print("adc : {:8} ".format(data))
        # MCP3008 の Vref に入れた電圧. ここでは 5V
        v = 5.0
        volts = convertVolts(data, v)
        # print("volts: {:8.2f}".format(volts))
        time.sleep(0.1)

if __name__ == "__main__":
    main()
