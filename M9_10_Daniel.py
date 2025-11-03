from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m910():
    SPEED = 550
    ACCELERATION = 350
    TURN_SPEED = 150
    TURN_ACCELERATION = 150
    await set_drivebase()
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)

    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    combined=1
    if combined==1:
        await DRIVE_BASE.straight(15)

        await DRIVE_BASE.turn(-42)#need
        await DRIVE_BASE.straight(500) #need
        LEFT_ATTACHMENT.reset_angle(0) #need
        await LEFT_ATTACHMENT.run_angle(100, -50) #need
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(100, 30)
        # await wait(500)
        RIGHT_ATTACHMENT.reset_angle(0) #need
        await RIGHT_ATTACHMENT.run_target(1000,2450) #need
        # await wait(500)
        await DRIVE_BASE.straight(60) #need
        # wait(500)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(100, 100)
        # wait(500)
        await DRIVE_BASE.straight(-215)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(1000, -500)
        # wait(500)
        await DRIVE_BASE.straight(70)
        # wait(500)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(1000,-1550)
        # wait(100)
        await DRIVE_BASE.curve(-500, 60)
        
    else:
        await RIGHT_ATTACHMENT.run_target(600,2450) #need

    DRIVE_BASE.use_gyro(False)