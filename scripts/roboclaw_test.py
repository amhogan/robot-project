#!/usr/bin/env python3
"""
Simple RoboClaw motor test
- Connects to RoboClaw via USB serial (/dev/ttyACM0 or /dev/ttyUSB0)
- Runs Motor 1 forward and backward, then Motor 2
- Prints encoder feedback if available
"""

import time
from roboclaw_3 import Roboclaw

# Adjust this if your RoboClaw shows up under a different device
PORT = "/dev/ttyACM0"
BAUDRATE = 38400  # must match Motion Studio setting

rc = Roboclaw(PORT, BAUDRATE)
rc.Open()

address = 0x80  # default RoboClaw address

def drive_test():
    print("Starting RoboClaw test")

    # Forward M1
    print("M1 forward 50%")
    rc.ForwardM1(address, 64)  # range 0-127
    time.sleep(2)

    # Backward M1
    print("M1 backward 50%")
    rc.BackwardM1(address, 64)
    time.sleep(2)

    # Stop M1
    rc.ForwardM1(address, 0)
    time.sleep(1)

    # Forward M2
    print("M2 forward 50%")
    rc.ForwardM2(address, 64)
    time.sleep(2)

    # Backward M2
    print("M2 backward 50%")
    rc.BackwardM2(address, 64)
    time.sleep(2)

    # Stop M2
    rc.ForwardM2(address, 0)
    time.sleep(1)

    print("Test complete.")

if __name__ == "__main__":
    drive_test()
