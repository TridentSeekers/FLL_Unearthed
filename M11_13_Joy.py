from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m11_13():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    SPEED = 550
    ACCELERATION = 350
    TURN_SPEED = 150
    TURN_ACCELERATION = 150
    await set_drivebase()
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)

    DRIVE_BASE.straight(790)
    DRIVE_BASE.turn(-60)
    DRIVE_BASE.straight(87)
    DRIVE_BASE.turn(-27)
    LEFT_ATTACHMENT.run_target(1000, -1300)
    DRIVE_BASE.turn(20)
    DRIVE_BASE.straight(-120)
    DRIVE_BASE.turn(99)
    RIGHT_ATTACHMENT.run_target(1000,-1000)
    DRIVE_BASE.straight(350)
    RIGHT_ATTACHMENT.run_target(1000,1000)
    DRIVE_BASE.turn(40)
    DRIVE_BASE.straight(-100)
    DRIVE_BASE.turn(100)
    DRIVE_BASE.straight(-800)