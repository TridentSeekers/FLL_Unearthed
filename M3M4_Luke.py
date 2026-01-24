from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m3m4():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    SPEED = 550
    ACCELERATION = 350
    TURN_SPEED = 150
    TURN_ACCELERATION = 150
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    watch = StopWatch()
    time1 = watch.time()
    await DRIVE_BASE.straight(850)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(90)
    RIGHT_ATTACHMENT.reset_angle(0)
    await RIGHT_ATTACHMENT.run_angle(800, -600)