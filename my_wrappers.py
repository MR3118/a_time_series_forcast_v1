from functools import wraps

import sys
import os

import atexit
import time
import psutil

# print "Welcome,current system is",os.name," 3 seconds late start to get data..."
time.sleep(3)

line_num = 1


# function of Get CPU State;
def getCPUstate(interval=1):
    return (" CPU: " + str(psutil.cpu_percent(interval)) + "%")


# function of Get Memory
def getMemorystate():
    phymem = psutil.virtual_memory()
    line = "Memory: %5s%% %6s/%s" % (
        phymem.percent,
        str(int(phymem.used / 1024 / 1024)) + "M",
        str(int(phymem.total / 1024 / 1024)) + "M"
    )
    return line
print(getCPUstate())
print(getMemorystate())