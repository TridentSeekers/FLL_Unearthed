"""
Library for text based code
"""

from pybricks.hubs import PrimeHub
from robot_config import DRIVE_BASE
from pybricks.tools import multitask
from library import battery_percentage
from pybricks.parameters import Color

hub = PrimeHub()

async def print_drivebase_settings():
    print('Default drivebase settings that are overridden in the config file')
    print('Speed, Acceleration, Turn, Turn Accel')
    print(DRIVE_BASE.settings())

async def print_battery_level():
    battery_voltage = hub.battery.voltage()
    print(f"Battery voltage: {battery_voltage} mV")
    battery_percentage(battery_voltage)
    percentage = battery_percentage(battery_voltage)
    print(f"Battery level: {percentage:.1f}%")

    if percentage < 20:
        hub.light.on(Color.RED)
        print("Low battery! Please charge.")
    elif percentage < 60:
        hub.light.on(Color.ORANGE)
        print("Warning 60% battery! Please charge.")
    else:
        hub.light.on(Color.GREEN)

