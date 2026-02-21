from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m567():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    SPEED = 800
    ACCELERATION = 600
    TURN_SPEED = 100
    TURN_ACCELERATION = 200
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    watch = StopWatch()
    time1 = watch.time()
    await DRIVE_BASE.straight(740)
    RIGHT_ATTACHMENT.reset_angle(0)
    await RIGHT_ATTACHMENT.run_angle(350, -350)
    await multitask(RIGHT_ATTACHMENT.run_target(500,350),DRIVE_BASE.turn(45))
    await DRIVE_BASE.straight(-100)
    await wait(50)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(41)
    await DRIVE_BASE.straight(300)
    LEFT_ATTACHMENT.reset_angle(0)
    await LEFT_ATTACHMENT.run_target(500,450)
    await DRIVE_BASE.straight(130)
    await wait(50)
    LEFT_ATTACHMENT.reset_angle(0)
    await LEFT_ATTACHMENT.run_target(300, -450)
    await DRIVE_BASE.straight(-400)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(-105)
    SPEED = 1000
    ACCELERATION = 1000
    TURN_SPEED = 100
    TURN_ACCELERATION = 200
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(False)
    await DRIVE_BASE.straight(-800)