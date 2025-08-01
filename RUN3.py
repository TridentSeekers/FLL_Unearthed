from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def run3():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)


    await DRIVE_BASE.turn(35)
    await DRIVE_BASE.straight(270)
    await DRIVE_BASE.turn(-30)
    await DRIVE_BASE.straight(1350)


