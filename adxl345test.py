# -*- coding: utf-8 -*-
#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import smbus
import time
from time import sleep
from time import perf_counter
import matplotlib.pyplot as plt
import csv
import datetime

# ADXL345 Class
class ADXL345:
    def __init__(self, addr):
        self.DevAdr = addr

    myBus = ""
    if GPIO.RPI_INFO["P1_REVISION"] == 1:
        myBus = 0
    else:
        myBus = 1

    b = smbus.SMBus(myBus)

    def setUp(self):
        self.b.write_byte_data(self.DevAdr, 0x2C, 0x0B)  # BandwidthRate
        self.b.write_byte_data(self.DevAdr, 0x31, 0x00)  # DATA_FORMAT 10bit 2g
        self.b.write_byte_data(self.DevAdr, 0x38, 0x00)  # FIFO_CTL OFF
        self.b.write_byte_data(self.DevAdr, 0x2D, 0x08)  # POWER_CTL Enable

    def getAccValue(self):
        x = self.getValue(0x32)
        y = self.getValue(0x34)
        z = self.getValue(0x36)
        return [x, y, z]

    def getValue(self, adr):
        tmp = self.b.read_byte_data(self.DevAdr, adr + 1)
        sign = tmp & 0x80
        tmp = tmp & 0x7F
        tmp = tmp << 8
        tmp = tmp | self.b.read_byte_data(self.DevAdr, adr)
        #       print '%4x' % tmp # debug

        if sign > 0:
            tmp = tmp - 32768

        return tmp

# MAIN
def main():

    # 書き込むファイルの作成
    dt_now = datetime.datetime.now()
    filename = './csv/' + dt_now.strftime('%m-%d_%H-%M-%S') + '.csv'
    print(dt_now.strftime('%m%d_%H-%M-%S'))

    # ファイルオープン
    f = open(filename, 'w')
    writer = csv.writer(f, lineterminator='\n')
    t_init = perf_counter()

    myADXL345_1 = ADXL345(0x1D)
    myADXL345_1.setUp()

    myADXL345_2 = ADXL345(0x53)
    myADXL345_2.setUp()
    csvlist = []
    # LOOP
    while perf_counter() - t_init < 10.0:
        # writer.writerow([perf_counter()])

        # print(time.time())
        x, y, z = myADXL345_1.getAccValue()
        # print("X=", x, "Y=", y, "Z=", z)

        # csvlist = []
        # csvlist.extend([perfcsvlist = []_counter(),x,y,z,"#1"])
        csvlist.append([perf_counter(),x,y,z,"#1"])
        # writer.writerow(csvlist)

        x2, y2, z2 = myADXL345_2.getAccValue()
        # print(time.time())
        # print("X2=", x2, "Y2=", y2, "Z2=", z2)

        # csvlist = []
        csvlist.append([perf_counter(),x2,y2,z2,"#2"])
        # writer.writerow(csvlist)
    
    # writer.writerow(csvlist)
    writer.writerows(csvlist)
    f.close()

if __name__ == "__main__":
    main()
