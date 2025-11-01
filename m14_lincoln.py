from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m14():
    SPEED = 550
    ACCELERATION = 350
    TURN_SPEED = 150
    TURN_ACCELERATION = 150
    await set_drivebase()
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    
    # The main program starts here.
    DRIVE_BASE.settings(straight_speed=850)
    await DRIVE_BASE.straight(295)
    DRIVE_BASE.settings(turn_rate=50)
    await DRIVE_BASE.turn(65)
    await DRIVE_BASE.straight(250)
    await DRIVE_BASE.straight(-150)
    await DRIVE_BASE.turn(-65)
    await DRIVE_BASE.straight(265)
    HUB.light.on(Color.GREEN)

