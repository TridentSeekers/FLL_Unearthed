from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m1m2():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    SPEED = 800
    ACCELERATION = 600
    TURN_SPEED = 500
    TURN_ACCELERATION = 400
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    watch = StopWatch()
    time1 = watch.time()
    await DRIVE_BASE.straight(678)
    DRIVE_BASE.reset(angle=0)
    SPEED = 1000
    ACCELERATION = 1000
    TURN_SPEED = 400
    TURN_ACCELERATION = 400
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    await DRIVE_BASE.turn(-46)
    SPEED = 700
    ACCELERATION = 650
    TURN_SPEED = 400
    TURN_ACCELERATION = 400
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    await wait(500)
    await DRIVE_BASE.straight(360)
    await wait(500)
    RIGHT_ATTACHMENT.reset_angle(0)
    await RIGHT_ATTACHMENT.run_angle(400, -350)
    await DRIVE_BASE.straight(-190)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(-45)
    for i in range(2):
        LEFT_ATTACHMENT.reset_angle(0) #need
        await LEFT_ATTACHMENT.run_target(900,-375)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_angle(1000, 800)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(95)
    SPEED = 1000
    ACCELERATION = 1000
    TURN_SPEED = 550
    TURN_ACCELERATION = 400
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    await DRIVE_BASE.straight(-800)