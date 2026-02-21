from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m3m4():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    SPEED = 450
    ACCELERATION = 350
    TURN_SPEED = 90
    TURN_ACCELERATION = 90
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    watch = StopWatch()
    time1 = watch.time()
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.straight(700)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(46)
    await DRIVE_BASE.straight(108)
    await DRIVE_BASE.turn(35)
    SPEED = 200
    ACCELERATION = 100
    TURN_SPEED = 90
    TURN_ACCELERATION = 90
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(99)
    LEFT_ATTACHMENT.reset_angle(0)
    await LEFT_ATTACHMENT.run_angle(50, -40)
    await wait(100)
    RIGHT_ATTACHMENT.reset_angle(0)
    await RIGHT_ATTACHMENT.run_angle(750, 1500)
    await RIGHT_ATTACHMENT.run_angle(1000, -600)
    await DRIVE_BASE.straight(-170)
    SPEED = 1000
    ACCELERATION = 1000
    TURN_SPEED = 750
    TURN_ACCELERATION = 850
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(120)
    await DRIVE_BASE.straight(800)
