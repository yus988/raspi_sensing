# -*- coding: utf-8 -*-
#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import smbus
import time

# ADXL345 Class
class ADXL345:
    DevAdr = 0x1d
    myBus = ""
    if GPIO.RPI_INFO['P1_REVISION'] == 1:
        myBus = 0
    else:
        myBus = 1
        
    b = smbus.SMBus(myBus)

    def setUp(self):
        self.b.write_byte_data(self.DevAdr, 0x2C, 0x0B) # BandwidthRate
        self.b.write_byte_data(self.DevAdr, 0x31, 0x00) # DATA_FORMAT 10bit 2g
        self.b.write_byte_data(self.DevAdr, 0x38, 0x00) # FIFO_CTL OFF
        self.b.write_byte_data(self.DevAdr, 0x2D, 0x08) # POWER_CTL Enable

    def getValueX(self):
        return self.getValue(0x32)

    def getValueY(self):
        return self.getValue(0x34)

    def getValueZ(self):
        return self.getValue(0x36)

    def getValue(self, adr):
        tmp = self.b.read_byte_data(self.DevAdr, adr+1)
        sign = tmp & 0x80
        tmp = tmp & 0x7F
        tmp = tmp<<8
        tmp = tmp | self.b.read_byte_data(self.DevAdr, adr)
#       print '%4x' % tmp # debug

        if sign > 0:
            tmp = tmp - 32768

        return tmp


class ADXL345_2:
    DevAdr = 0x53
    
    myBus = ""
    if GPIO.RPI_INFO['P1_REVISION'] == 1:
        myBus = 0
    else:
        myBus = 1
        
    b = smbus.SMBus(myBus)

    def setUp(self):
        self.b.write_byte_data(self.DevAdr, 0x2C, 0x0B) # BandwidthRate
        self.b.write_byte_data(self.DevAdr, 0x31, 0x00) # DATA_FORMAT 10bit 2g
        self.b.write_byte_data(self.DevAdr, 0x38, 0x00) # FIFO_CTL OFF
        self.b.write_byte_data(self.DevAdr, 0x2D, 0x08) # POWER_CTL Enable

    def getValueX(self):
        return self.getValue(0x32)

    def getValueY(self):
        return self.getValue(0x34)

    def getValueZ(self):
        return self.getValue(0x36)

    def getValue(self, adr):
        tmp = self.b.read_byte_data(self.DevAdr, adr+1)
        sign = tmp & 0x80
        tmp = tmp & 0x7F
        tmp = tmp<<8
        tmp = tmp | self.b.read_byte_data(self.DevAdr, adr)
#       print '%4x' % tmp # debug

        if sign > 0:
            tmp = tmp - 32768

        return tmp
#   tmp = self.b.read_word_data(self.DevAdr, adr)

# with open('test.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow([0, 1, 2])
#     writer.writerow(['a', 'b', 'c'])

# MAIN
myADXL345 = ADXL345()
myADXL345.setUp()

myADXL345_2 = ADXL345_2()
myADXL345_2.setUp()

# LOOP
for a in range(1000):

    print(time.time())

    x = myADXL345.getValueX()
    y = myADXL345.getValueY()
    z = myADXL345.getValueZ()
    

    print("X=", x)
    # print(time.time())
    print("Y=", y)
    # print(time.time())
    print("Z=", z)
    
    x2 = myADXL345_2.getValueX()
    y2 = myADXL345_2.getValueY()
    z2 = myADXL345_2.getValueZ()
    
    # print(time.time())
    print("X2=", x2)
    print("Y2=", y2)
    print("Z2=", z2)
  
    # os.system("clear")
    # time.sleep(1)

