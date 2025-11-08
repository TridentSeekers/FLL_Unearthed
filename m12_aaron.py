from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT
from library import set_drivebase

async def m12():
    # The main program starts here.
    SPEED = 650
    ACCELERATION = 650
    TURN_SPEED = 150
    TURN_ACCELERATION = 150
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)

    await DRIVE_BASE.straight(600)
    # await DRIVE_BASE.turn(80)
    wait(50)
    await RIGHT_ATTACHMENT.run_angle(300, 80)
    await RIGHT_ATTACHMENT.run_angle(350, -250)
    DRIVE_BASE.use_gyro(False)
    await DRIVE_BASE.straight(-500)
