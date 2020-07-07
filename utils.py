import os, re
from config import *


def list_devices():
    adb_devs = os.popen("adb devices").read()
    devices = re.findall("[0-9A-Z]{6,20}", adb_devs)
    return devices


def launch_adb(command, device):
    command = str(command).format(SERIAL=device, PATH_TO_APK=PATH_TO_APK, APK=APK,
                                  TIMEZONE=TIMEZONE, PACKAGE=PACKAGE)
    print("Running: " + command)
    print(os.popen(command).read())
