from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m3m14():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    SPEED = 450
    ACCELERATION = 700
    TURN_SPEED = 100
    TURN_ACCELERATION = 100
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    watch = StopWatch()
    time1 = watch.time()
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(7)
    await DRIVE_BASE.straight(535)
    RIGHT_ATTACHMENT.reset_angle(0)
    await RIGHT_ATTACHMENT.run_target(1000,-200)
    await wait(100)
    await DRIVE_BASE.straight(245)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(87)
    await wait(100)
    SPEED = 200
    ACCELERATION = 200
    TURN_SPEED = 100
    TURN_ACCELERATION = 100
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    await multitask(RIGHT_ATTACHMENT.run_target(1000,200), DRIVE_BASE.straight(715))
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(-62)
    await DRIVE_BASE.straight(200)
    DRIVE_BASE.use_gyro(False)
    # DRIVE_BASE.reset(angle=0)
    # await DRIVE_BASE.turn(-45)
    # await wait(100)
    