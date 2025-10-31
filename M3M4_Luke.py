from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch

from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m3m4():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)

    combined=0
    if (combined==1):
        await DRIVE_BASE.straight(800)

    else:
        await DRIVE_BASE.straight(760)
        await DRIVE_BASE.turn(83)
        DRIVE_BASE.settings(straight_speed=100)
        DRIVE_BASE.settings(straight_acceleration=100)
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.straight(190)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(800, 700)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(70, -25)
        await DRIVE_BASE.straight(-190)


