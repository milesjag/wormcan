import time
import board
import busio
import adafruit_mpr121
import logging

def get_logger():
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger()
    log.debug("Logging initialized")
    return log

log = get_logger()

def run_touch(touchpad):
    touch_count = 0
    num_sensors= [1]
    log.debug(f"Number of sensors set to {len(num_sensors)}")
    log.debug("Running touch sensors...")
    while True:
        for i in num_sensors:
            touch_count += 1
            log.debug(f"Input {i} - Baseline: {touchpad.baseline_data(i)} Filtered: {touchpad.filtered_data(i)}, Contact: {touchpad.is_touched(i)}")


if __name__ == "__main__":
    log.debug("Imports successful")
    i2c = busio.I2C(board.SCL, board.SDA)
    log.debug("I2C setup successful")
    mpr121 = adafruit_mpr121.MPR121(i2c)
    log.debug("MPR121 setup successful")
    run_touch(mpr121)
