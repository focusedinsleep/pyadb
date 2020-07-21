import os
import platform
import re

from config import *

ADB_COMMAND = ''


# TODO:
# 1. get os
# 2. setup os specific commands
def list_devices():
    global ADB_COMMAND
    if platform.system() == 'Windows':
        pwd = os.popen("cd").read().strip()
        ADB_COMMAND = WINDOWS_ADB.format(CURRENT_DIR=pwd) + 'adb.exe'
    adb_devs = os.popen(ADB_COMMAND + " devices").read()
    serials = re.findall("[0-9A-Z]{6,20}", adb_devs)
    devices = []
    for sl in serials:
        model_ = os.popen(f'{ADB_COMMAND} -s {sl} shell getprop ro.product.model').read().strip()
        devices.append(sl + " " + model_)
    return devices


def launch_adb(command, device):
    command = str(command).format(ADB_COMMAND=ADB_COMMAND, SERIAL=device, PATH_TO_APK=PATH_TO_APK, APK=APK,
                                  TIMEZONE=TIMEZONE, PACKAGE=PACKAGE)
    print("Running: " + command)
    os.system(command)
