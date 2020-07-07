import os, re
from config import *


def list_devices():
    adb_devs = os.popen("adb devices").read()
    serials = re.findall("[0-9A-Z]{6,20}", adb_devs)
    devices = []
    for sl in serials:
        model_ = os.popen(f'adb -s {sl} shell getprop ro.product.model').read().strip()
        devices.append(sl + " " + model_)
    return devices


def launch_adb(command, device):
    command = str(command).format(SERIAL=device, PATH_TO_APK=PATH_TO_APK, APK=APK,
                                  TIMEZONE=TIMEZONE, PACKAGE=PACKAGE)
    print("Running: " + command)
    print(os.popen(command).read())
