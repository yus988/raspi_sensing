############################################################
### Example for Communicating with ADXL362 Accelerometer ###
### for Raspberry Pi using ADXL362.py                    ###
###                                                      ###
### Authors: Sam Zeckendorf                              ###
###          Nathan Tarrh                                ###
###    Date: 3/29/2014                                   ###
############################################################

# -*- coding: utf-8 -*-
"""
matplotlibでリアルタイムプロットする例

無限にsin関数をplotし続ける
"""
from __future__ import unicode_literals, print_function

import numpy as np
import matplotlib.pyplot as plt

import ADXL362
import time


def main():
    accel_0 = ADXL362.ADXL362(0, 0)
    accel_0.begin_measure()
    accel_1 = ADXL362.ADXL362(0,1)
    accel_1.begin_measure()

    # print (accel_0.read_xyz())
    # print (accel_1.read_xyz())
    fig, ax = plt.subplots(1, 1)
    x = np.arange(0, 100,1)
    y = np.zeros(100)
    # print(y)
    lines, = ax.plot(x, y)

    while True:
        x += 1
        # y = np.sin(x)
        # y = np.append(y, i)
        # y = 0.2
        y = np.append(y, accel_1.read_xyz()[0])
        y = np.delete(y, 0)
        print(y)

        lines.set_data(x, y)
        ax.set_xlim((x.min(), x.max()))
        ax.set_ylim((y.min(), y.max()))
        plt.pause(.001)

        # time.sleep(2)

if __name__ == "__main__":
    main()
