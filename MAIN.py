from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait
from measurements import left_attach_measurements, push_measurements, right_attach_measurements
from library import set_drivebase
from RUN1 import run1
from RUN2 import run2
from RUN3 import run3
from RUN4 import run4
from RUN5 import run5
from RUN6 import run6
from RUN7 import run7
from RUN8 import run8
from RUN9 import run9

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
    await print_drivebase_settings()
    # Override these settings. Note pybricks is conservative with speeds.
    # The default speeds are about 40% of what the motors can handle
    # You probably can double the default speeds in the robot_config file.
    # Conversely the accelration values pybricks creates tend to be too high
    # If your wheels slip your distances will be off. Lower accelration as needed
    # in the robot_config file to eliminate wheel slippage. These values will depend on wheel choice, center of gravity of your robot and robot weight.
    await print_battery_level()
    await set_drivebase()
    # Add the programs (Missons) below they will appear in the order placed
    # Missions will need to be imported, see example missions/utility programs
    # below
    await add_program(run1, '1', Color.GREEN)
    await add_program(run2, '2', Color.GREEN)
    await add_program(run3, '3', Color.GREEN)
    await add_program(run4, '4', Color.GREEN)
    await add_program(run5, '5', Color.GREEN)
    await add_program(run6, '6', Color.GREEN)
    await add_program(run7, '7', Color.GREEN)
    await add_program(run8, '8', Color.GREEN)
    await add_program(run9, '9', Color.GREEN)
    await add_program(push_measurements, 'P', Color.BLUE)
    await add_program(left_attach_measurements, 'L', Color.BLUE)
    await add_program(right_attach_measurements, 'R', Color.BLUE)

    # Launch the user interface
    await user_interface()


run_task(main())