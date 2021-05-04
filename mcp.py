#!/usr/bin/env python
from gpiozero import MCP3008
import time
Vref = 3.29476

while True:
    pot = MCP3008(channel=5)
    print(str(pot.value * Vref) + "V")
    time.sleep(0.1)