# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:56:07 2020

@author: Prabal
"""
import sys
import shutil
def check_disk_usage(disk,min_absolute,min_percent):
    du=shutil.disk_usage(disk)
    percent_free=100*du.free/du.total
    gigabytes_free=du.free/2**30
    #condition checking for storage
    #checking condition
    if percent_free<min_percent or gigabytes_free<min_absolute:
        return False
    return True
if not check_disk_usage("/",2,10):
    print("Error happened")
    sys.exit(1)
print("ok")
sys.exit(0)