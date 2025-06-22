from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

async def run2():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    await DRIVE_BASE.straight(200)
    await DRIVE_BASE.curve(100, 1080)
    await DRIVE_BASE.straight(-200)
