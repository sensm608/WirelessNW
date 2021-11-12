#!/usr/bin/python3

import pyfirmata as pf
import time

board = pf.Arduino('/dev/ttyACM0')
pin13 = board.get_pin('d:13:o')
time.sleep(1)
pin13.write(1)
time.sleep(1)
pin13.write(0)
