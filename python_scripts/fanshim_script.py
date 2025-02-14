#!/usr/bin/python3

import time


try:
    from fanshim import FanShim
except ImportError as e:
    print("fanshim module not found, please install the fanshim package")
    print("[+] sudo pip install fanshim --break-system-packages")

fan = FanShim()
fan.auto = False # disable automatic control

# Set temperature thresholds
TEMP_ON = 55
TEMP_OFF = 35

def get_cpu_temp():
    # Read CPU temperature
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
    return float(temp) / 1000

def control_fan():
    fan_on = False

    while True:
        temp = get_cpu_temp()

        if temp >= TEMP_ON and not fan_on:
            fan.set_fan(True)
            fan_on = True
        elif temp <= TEMP_OFF and fan_on:
            fan.set_fan(False)
            fan_on = False

        time.sleep(5)


control_fan()