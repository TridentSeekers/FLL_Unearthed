from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch

from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m910():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    # DRIVE_BASE.reset(distance=0)
    DRIVE_BASE.straight(30)
    # wait(500)
    # LEFT_ATTACHMENT.reset_angle(0)
    # LEFT_ATTACHMENT.run_target(200, -60)
    # wait(500)
    DRIVE_BASE.reset(angle=0) #need
    DRIVE_BASE.turn(-43)#need

    # DRIVE_BASE.reset(distance=0)
    DRIVE_BASE.straight(485) #need
    # wait(500)
    LEFT_ATTACHMENT.reset_angle(0) #need
    LEFT_ATTACHMENT.run_angle(500, -80) #need
    # wait(100)
    # LEFT_ATTACHMENT.reset_angle(0)
    # LEFT_ATTACHMENT.run_target(1000,-180)
    # wait(500)
    LEFT_ATTACHMENT.reset_angle(0)
    LEFT_ATTACHMENT.run_target(200, 30)
    wait(500)
    RIGHT_ATTACHMENT.reset_angle(0) #need
    RIGHT_ATTACHMENT.run_target(1000,2450) #need
    wait(500)
    DRIVE_BASE.straight(60) #need
    wait(500)
    LEFT_ATTACHMENT.reset_angle(0)
    LEFT_ATTACHMENT.run_target(700, 300)
    wait(500)
    DRIVE_BASE.straight(-205)
    RIGHT_ATTACHMENT.reset_angle(0)
    RIGHT_ATTACHMENT.run_target(1000, -500)
    wait(500)
    DRIVE_BASE.straight(70)
    wait(500)
    RIGHT_ATTACHMENT.reset_angle(0)
    RIGHT_ATTACHMENT.run_target(1000,-1550)
    wait(100)
    DRIVE_BASE.curve(-500, 60)
