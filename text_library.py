"""
Library for text based code
"""

from pybricks.hubs import PrimeHub
from robot_config import DRIVE_BASE, Robot_name
from pybricks.tools import wait
from library import battery_percentage
from pybricks.parameters import Color

hub = PrimeHub()

async def print_drivebase_settings():
    print("Robot Name: ", Robot_name)
    print('Default drivebase settings that are overridden in the config file')
    print(f"Speed: {DRIVE_BASE.settings()[0]} mm/s, Acceleration: {DRIVE_BASE.settings()[1]} mm/s²" )
    print(f"Turn Rate: {DRIVE_BASE.settings()[2]} deg/s, Turn Accel: {DRIVE_BASE.settings()[3]} deg/s²" )

async def print_battery_level():

    chargerstatus = hub.charger.status()
    if chargerstatus == 0:
        print("Charger Status: Not connected")
    elif chargerstatus == 1:
        print("Charger Status: Charging")
    elif chargerstatus == 2:
        print("Charger Status: Full")
    elif chargerstatus == 3:
        print("Charger Status: Error")
    else:
        # This should never happen, but just in case
        print("Charger Status: Unknown")   

    battery_voltage = hub.battery.voltage()
    print(f"Battery voltage: {battery_voltage} mV")
    battery_percentage(battery_voltage)
    percentage = battery_percentage(battery_voltage)
    print(f"Battery level: {percentage:.1f}%")
    

    if percentage < 40:
        hub.light.on(Color.RED)
        print("Low battery! Must charge.")
    elif percentage < 70:
        hub.light.on(Color.ORANGE)
        print("Warning 70% battery!")
    else:
        hub.light.on(Color.GREEN)

 