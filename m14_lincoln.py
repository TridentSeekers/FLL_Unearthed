from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m14():
    # The main program starts here.
    DRIVE_BASE.settings(straight_speed=850)
    await DRIVE_BASE.straight(295)
    DRIVE_BASE.settings(turn_rate=50)
    await DRIVE_BASE.turn(65)
    await DRIVE_BASE.straight(250)
    await DRIVE_BASE.straight(-150)
    await DRIVE_BASE.turn(-65)
    await DRIVE_BASE.straight(265)
    HUB.light.on(Color.GREEN)

