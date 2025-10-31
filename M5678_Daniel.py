from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch

from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT




async def move_motor_down():
    LEFT_ATTACHMENT.reset_angle(0) #need
    LEFT_ATTACHMENT.run_angle(1000, 100, wait= False) #need
    RIGHT_ATTACHMENT.reset_angle(0) #need
    RIGHT_ATTACHMENT.run_target(1000,-80, wait= False) #need


async def move_motor_up():
    LEFT_ATTACHMENT.reset_angle(0) #need
    LEFT_ATTACHMENT.run_angle(500, -70, wait= False) #need
    RIGHT_ATTACHMENT.reset_angle(0) #need
    RIGHT_ATTACHMENT.run_target(500,70, wait= False) #need

async def m5678():
    # await multitask(wait(1000), move_motor_down())
    # await multitask(wait(1000), move_motor_up())
    # await multitask(wait(1000), move_motor_down())
    # await multitask(wait(1000), move_motor_up())
    # await multitask(wait(1000), move_motor_down())
    # await multitask(wait(1000), move_motor_up()) 
    combined=1
    if (combined ==1):

        await DRIVE_BASE.straight(400)   

        for i in range(2):
            LEFT_ATTACHMENT.reset_angle(0) #need
            await LEFT_ATTACHMENT.run_target(1000,130)
            wait(200)            
            LEFT_ATTACHMENT.reset_angle(0) #need
            await LEFT_ATTACHMENT.run_target(1000,-130)
        LEFT_ATTACHMENT.reset_angle(0) #need
        await LEFT_ATTACHMENT.run_target(1000,170)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-90)
        await DRIVE_BASE.straight(210)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(100)
        await DRIVE_BASE.straight(340)
        # LEFT_ATTACHMENT.reset_angle(0) #need
        # await LEFT_ATTACHMENT.run_target(1000,130)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-47)
        await DRIVE_BASE.turn(15)
        await DRIVE_BASE.straight(-95)
        await DRIVE_BASE.turn(80)
        await DRIVE_BASE.straight(55)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(700, -55)
        await DRIVE_BASE.turn(-60)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(700, 75)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(700, -105)
        await DRIVE_BASE.turn(40)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(1000, -150)
        await DRIVE_BASE.straight(87)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(500, 300)
        await DRIVE_BASE.straight(-100)
        await DRIVE_BASE.turn(43)
        await DRIVE_BASE.straight(400)
        await DRIVE_BASE.straight(-430)
        await DRIVE_BASE.turn(-100)
        await DRIVE_BASE.straight(-700)
    else:
        # # LEFT_ATTACHMENT.reset_angle(0) #need
        # # await LEFT_ATTACHMENT.run_target(1000,-10)
        # # DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-30)
        
        


