# -*- coding: utf-8 -*-

import smbus
import math
from time import sleep
from time import perf_counter
import time
import matplotlib.pyplot as plt

#mpu6050のデバイスアドレス（決まっている）
DEV_ADDR = 0x68

ACCEL_XOUT = 0x3b
ACCEL_YOUT = 0x3d
ACCEL_ZOUT = 0x3f
TEMP_OUT = 0x41
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47

PWR_MGMT_1 = 0x6b
PWR_MGMT_2 = 0x6c   

# sudo i2cdetect 0 : Error: Could not open file `/dev/i2c-0' or `/dev/i2c/0'
# sudo i2cdetect 1 : I will probe file /dev/i2c-1
# エラーの出ない方がバス番号(0 か 1)
# コネクションオブジェクトを取得
bus = smbus.SMBus(1)

# write_byte_data(アドレス, コマンド, 1バイトの値)
# スリープを解除 多分（最初はスリープしている）
bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)

# make plot
times = [0 for i in range(60)]
axs = [0 for i in range(60)]

time = 0
ax = 0

# initialize matplotlib
plt.ion()
plt.figure()
li_x, = plt.plot(times, axs) # need " , "
#li_y, = plt.plot(times, ays) # need " , "
#li_z, = plt.plot(times, azs) # need " , "

#plt.xlim(-1,1)
plt.ylim(-2,2)
plt.xlabel("time")
plt.ylabel("ax,ay,az")
plt.title("ax,ay,az real time plot")


def read_word(adr):
    
    high = bus.read_byte_data(DEV_ADDR, adr)
    low = bus.read_byte_data(DEV_ADDR, adr+1)
    val = (high << 8) + low
    return val

def read_word_sensor(adr):
    #２バイトデータから　１ワードデータへデコードする
    val = read_word(adr)
    if (val >= 0x8000):  return -((65535 - val) + 1)
    else:  return val

def get_temp():
    # 温度を算出する
    temp = read_word_sensor(TEMP_OUT)
    x = temp / 340 + 36.53      # data sheet(register map)記載の計算式.
    return x

def getGyro():
    # ３軸 角速度を算出する
    x = read_word_sensor(GYRO_XOUT)/ 131.0
    y = read_word_sensor(GYRO_YOUT)/ 131.0
    z = read_word_sensor(GYRO_ZOUT)/ 131.0
    return [x, y, z]

def getAccel():
    # ３軸 加速度を算出する
    x = read_word_sensor(ACCEL_XOUT)/ 16384.0
    y= read_word_sensor(ACCEL_YOUT)/ 16384.0
    z= read_word_sensor(ACCEL_ZOUT)/ 16384.0
    return [x, y, z]

# Define initial time
t_init = perf_counter()

while perf_counter() - t_init < 60.0 :
    t = perf_counter() - t_init
    # ３軸 加速度を算出し出力する
    ax, ay, az = getAccel()
    print ('{0:4.3f}, {1:4.3f}, {2:4.3f}, {3:4.3f}'
           .format(t, ax, ay, az))    

    #最新のデータを追加すると同時に最初のデータを削除する
    times.append(t)
    times.pop(0)
    axs.append(ax)
    axs.pop(0)
    #ays.append(ax)
    #ays.pop(0)    
    #azs.append(ax)
    #azs.pop(0)    
    
    
    # 区間プロットする
    li_x.set_xdata(times)
    li_x.set_ydata(axs)
    plt.xlim(min(times), max(times))
    plt.draw() # plt.ion()に対応 （plt.show()ではない）

    plt.pause(0.01)
    sleep(0.02)