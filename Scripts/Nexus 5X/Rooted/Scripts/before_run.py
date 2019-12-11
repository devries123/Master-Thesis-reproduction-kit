import time
import random
import datetime


# noinspection PyUnusedLocal
def main(device, *args, **kwargs):
    device.shell('settings put system screen_brightness_mode 0')
    device.shell('settings put system screen_brightness 0')
