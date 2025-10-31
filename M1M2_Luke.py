from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch

from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m1m2():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)

    combined=0
    if (combined ==1):
        #Go forward to Mission 1
        await DRIVE_BASE.straight(700)
        await DRIVE_BASE.straight(-140)
        await DRIVE_BASE.straight(100)
        #Turn and Go forward to Mission 2
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-45)
        await DRIVE_BASE.straight(210)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_angle(150, -250)
    #Backward to do Mission 1
        await DRIVE_BASE.straight(-140)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-46)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_angle(600, 100)
        #Go get brush
        await DRIVE_BASE.straight(65)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_angle(70, -80)
        
        await DRIVE_BASE.straight(-150)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-60)
        await DRIVE_BASE.straight(600)

    else:
        await DRIVE_BASE.straight(650)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-42)
        await DRIVE_BASE.straight(210)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_angle(150, -250)
        await DRIVE_BASE.straight(-200)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-30)
        await DRIVE_BASE.straight(75)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_angle(40, -80)
        await DRIVE_BASE.curve(-260,-160)

