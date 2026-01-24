from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m7():
    # Ensure drivebase/gyro are configured at runtime (not at import time)
    await set_drivebase()
    DRIVE_BASE.use_gyro(True)

    # run_until_stalled is a blocking call that operates the motor until it stalls.
    # Make sure we are not instantiating motors here (they come from robot_config)
    # RIGHT_ATTACHMENT.reset_angle(0)
    # RIGHT_ATTACHMENT.run_until_stalled(300, duty_limit=50)
    # await DRIVE_BASE.straight(100)
    # RIGHT_ATTACHMENT.reset_angle(0)
    # await RIGHT_ATTACHMENT.run_target(500, 250)
    # DRIVE_BASE.reset(distance=0, angle=0)
    # await DRIVE_BASE.straight(45)
    RIGHT_ATTACHMENT.reset_angle(0)
    # await RIGHT_ATTACHMENT.run_target(500, 300)
    await RIGHT_ATTACHMENT.run_target(200, 120)
    await DRIVE_BASE.straight(50)
    RIGHT_ATTACHMENT.reset_angle(0)
    await RIGHT_ATTACHMENT.run_until_stalled(-1000, duty_limit=50)
    # DRIVE_BASE.reset(distance=0, angle=0)