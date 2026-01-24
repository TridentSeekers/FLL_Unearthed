# Appreciate https://github.com/MonongahelaCryptidCooperative/FLL-2025-2026
# The code is modified for Trident Seekers' robots.
import M1M2_Vincent
from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait
from measurements import left_attach_measurements, push_measurements, right_attach_measurements
from library import set_drivebase, battery_percentage
# Pre-set 9 runs. Please modify subroutines RUN1 to RUN9.
from RUN_TEST import run_test
from M5678_Daniel import m5678
from M9_10_Daniel import m910
from M11_13_Joy import m11_13
from M3M4_Luke import m3m4
from M1M2_Luke import m1m2
from m14_lincoln import m14
from m12_aaron import m12
from M7testforrun_until_stalled import m7
from M1M2_Vincent import m1m2 as M1M2_Vincent
from text_library import print_drivebase_settings, print_battery_level
from ui import add_program, user_interface

async def main():
    
    # Must be paired at starup or will crash. Disconnect block if not wanted
    # Note the code is provided disconnected.

    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        wait(0),
    )
    # Print to consule the default drivebase settings
    await set_drivebase()
    await print_drivebase_settings()
    # Override these settings. Note pybricks is conservative with speeds.
    # The default speeds are about 40% of what the motors can handle
    # You probably can double the default speeds in the robot_config file.
    # Conversely the accelration values pybricks creates tend to be too high
    # If your wheels slip your distances will be off. Lower accelration as needed
    # in the robot_config file to eliminate wheel slippage. These values will depend on wheel choice, center of gravity of your robot and robot weight.
    await print_battery_level()

 
    
    
    
    # Add the programs (Missons) below they will appear in the order placed
    # Missions will need to be imported, see example missions/utility programs
    # below
    #await add_program(print_battery_level, 'B', Color.WHITE)
    await add_program(run_test, 'T', Color.WHITE)
    await add_program(m910, '1', Color.GREEN)
    await add_program(m5678, '2', Color.GREEN)
    await add_program(m11_13, '3', Color.GREEN)
    await add_program(m12, '4', Color.GREEN)
    await add_program(m1m2, '5', Color.GREEN)
    await add_program(m3m4, '6', Color.GREEN)
    await add_program(m14, '7', Color.GREEN)
    await add_program(m7, '8', Color.GREEN)
    await add_program(M1M2_Vincent, '9', Color.GREEN)

    await add_program(push_measurements, 'P', Color.BLUE)
    await add_program(left_attach_measurements, 'L', Color.BLUE)
    await add_program(right_attach_measurements, 'R', Color.BLUE)

    # Launch the user interface
    await user_interface()


run_task(main())