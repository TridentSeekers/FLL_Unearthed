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
    await DRIVE_BASE.straight(480)
    DRIVE_BASE.reset(angle=0)
    SPEED = 1000
    ACCELERATION = 1000
    TURN_SPEED = 400
    TURN_ACCELERATION = 250
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    await DRIVE_BASE.turn(45)
    SPEED = 450
    ACCELERATION = 550
    TURN_SPEED = 400
    TURN_ACCELERATION = 400
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    await DRIVE_BASE.straight(139)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(-82)
    await wait(100)
    await DRIVE_BASE.straight(400)
    RIGHT_ATTACHMENT.reset_angle(0)
    await RIGHT_ATTACHMENT.run_angle(350, -350)
    await DRIVE_BASE.straight(-200)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.turn(-55)
    await DRIVE_BASE.straight(270)
    await wait(100)
    LEFT_ATTACHMENT.reset_angle(0) #need
    await LEFT_ATTACHMENT.run_target(300,-250)
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.straight(-200)
    await DRIVE_BASE.turn(105)
    SPEED = 1000
    ACCELERATION = 1000
    TURN_SPEED = 550
    TURN_ACCELERATION = 400
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    await DRIVE_BASE.straight(-800)
    DRIVE_BASE.use_gyro(False)