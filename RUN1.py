from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT



async def run1():
    await wait(0)
    # Just a demo to show off the drivebase as well as music, icons,
    # and multitasking
    # Turn button yellow; and beep/wait so hands are out of the way
    HUB.light.on(Color.YELLOW)
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(100)
    await wait(0)
    # await DRIVE_BASE.straight(300)
    # await DRIVE_BASE.turn(180)
    # await DRIVE_BASE.straight(300)
    # await DRIVE_BASE.turn(-180)
    # await DRIVE_BASE.straight(-100)
    DRIVE_BASE.use_gyro(False)

