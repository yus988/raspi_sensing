############################################################
### Example for Communicating with ADXL362 Accelerometer ###
### for Raspberry Pi using ADXL362.py                    ###
###                                                      ###
### Authors: Sam Zeckendorf                              ###
###          Nathan Tarrh                                ###
###    Date: 3/29/2014                                   ###
############################################################

import ADXL362
import time

accel_0 = ADXL362.ADXL362(0,0)
accel_1 = ADXL362.ADXL362(0,1)
accel_0.begin_measure()
accel_1.begin_measure()

while True:
    # print (accel_0.read_xyz())
    print (accel_1.read_xyz()[0])
    # print (accel_0.read_y())
    # time.sleep(0.1)
