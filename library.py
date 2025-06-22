from pybricks.tools import multitask, run_task, wait

from robot_config import ACCELERATION, DRIVE_BASE, HUB, SPEED, TURN_ACCELERATION, TURN_SPEED

async def set_drivebase():
    await wait(0)
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)

def battery_percentage(voltage):
      # Assuming a 100% charge is around 8300 mV and a 0% charge is around 6000 mV
      max_voltage = 8300
      min_voltage = 5500
      percentage = (voltage - min_voltage) / (max_voltage - min_voltage) * 100
      return max(0, min(100, percentage))  # Ensure the percentage is between 0 and 100



async def main():
    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        wait(0),
    )


run_task(main())