import time
import board
import busio
import adafruit_mpr121
import logging
import datetime
from typing import Dict, List, Union

def get_logger():
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger()
    log.debug("Logging initialized")
    return log

log = get_logger()

def measure_pin_activity(touchpad, pin_id) -> Dict[str, Union[int, float]]:
    """
    Measure electical activity data for the supplied pin ID and
    return results object
    """
    return {
            "pin_id": pin_id,
            "baseline": touchpad.baseline_data(pin_id),
            "filtered": touchpad.filtered_data(pin_id),
            "is_touched": touchpad.is_touched(pin_id)
            }

def measure_touchpad_activity(touchpad):
    """
    Measure electical activity data for all active pins
    and return results object
    """
    measured_dt = datetime.datetime.now(datetime.timezone.utc)
    active_sensors= range(12)
    results_set = []
    log.debug(f"Number of active sensors: {len(active_sensors)}")
    log.debug("Running touchpad activity measurements...")
    for pin_id in active_sensors:
        results_set.append(
                {
                    "measured_at": measured_dt,
                    **measure_pin_activity(touchpad, pin_id)
                }
        )
    log.debug("Completed touchpad activity measurements") 
    return results_set
    

def initialize_touchpad() -> adafruit_mpr121.MPR121:
    log.debug("Imports successful")
    i2c = busio.I2C(board.SCL, board.SDA)
    log.debug("I2C setup successful")
    mpr121 = adafruit_mpr121.MPR121(i2c)
    log.debug("MPR121 setup successful")
    return mpr121

if __name__ == "__main__":
    touchpad = initialize_touchpad()
    results = measure_touchpad_activity(touchpad)
    print(results)
