from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
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

    SPEED = 550
    ACCELERATION = 550
    TURN_SPEED = 450
    TURN_ACCELERATION = 150
    await set_drivebase()
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    watch = StopWatch()
    time1 = watch.time() 
    combined=0
    if (combined ==1):

        await DRIVE_BASE.straight(400)   

        for i in range(2):
            LEFT_ATTACHMENT.reset_angle(0) #need
            await LEFT_ATTACHMENT.run_target(1200,130)
            wait(200)            
            LEFT_ATTACHMENT.reset_angle(0) #need
            await LEFT_ATTACHMENT.run_target(1000,-130)
        LEFT_ATTACHMENT.reset_angle(0) #need
        await LEFT_ATTACHMENT.run_target(1200,170)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-90)
        await DRIVE_BASE.straight(210)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(97)
        await DRIVE_BASE.straight(357)
        # LEFT_ATTACHMENT.reset_angle(0) #need
        # await LEFT_ATTACHMENT.run_target(1000,130)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-47)
        await DRIVE_BASE.turn(15)
        await DRIVE_BASE.straight(-85)
        await DRIVE_BASE.turn(80)
        await DRIVE_BASE.straight(55)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(700, -30)
        await DRIVE_BASE.turn(-70)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(700, 75)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(700, -105)
        await DRIVE_BASE.turn(50)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(1000, -150)
        await DRIVE_BASE.straight(87)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(500, 300)
        await DRIVE_BASE.straight(-100)
        await DRIVE_BASE.turn(43)
        await DRIVE_BASE.straight(400)
        await DRIVE_BASE.straight(-400)
        await DRIVE_BASE.turn(-80)
        await DRIVE_BASE.straight(-700)
    else:
        await DRIVE_BASE.straight(400)   
        # Finish three times silo
        for i in range(2):
            LEFT_ATTACHMENT.reset_angle(0) #need
            await LEFT_ATTACHMENT.run_target(1200,130)
            wait(200)            
            LEFT_ATTACHMENT.reset_angle(0) #need
            await LEFT_ATTACHMENT.run_target(1000,-130)
        LEFT_ATTACHMENT.reset_angle(0) #need
        await LEFT_ATTACHMENT.run_target(1200,170)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-90)
        # Go to M5
        await DRIVE_BASE.straight(200)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(95)
        await DRIVE_BASE.straight(355)
        # Turn left to finish M5
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-55)
        
        await multitask(LEFT_ATTACHMENT.run_target(200, -75),DRIVE_BASE.turn(46))
        await DRIVE_BASE.straight(40)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(55)
        # LEFT_ATTACHMENT.reset_angle(0)
        # # LEFT_ATTACHMENT.run_target(200, -20)
        
        # await multitask(LEFT_ATTACHMENT.run_target(200, -45),DRIVE_BASE.straight(30))
        # # await DRIVE_BASE.straight(25)
        # # LEFT_ATTACHMENT.reset_angle(0)
        # # # await LEFT_ATTACHMENT.run_target(700, -45)
        
        # await DRIVE_BASE.turn(-75)
        # # await multitask(LEFT_ATTACHMENT.run_target(700, -45),DRIVE_BASE.turn(-85))

        # LEFT_ATTACHMENT.reset_angle(0)
        # # # await LEFT_ATTACHMENT.run_target(700, 75)
        # # LEFT_ATTACHMENT.reset_angle(0)
        # await multitask(LEFT_ATTACHMENT.run_target(300, -105),DRIVE_BASE.turn(75))
        # # await LEFT_ATTACHMENT.run_target(700, -105)
        # # await DRIVE_BASE.turn(50)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(1000, -150)
        await DRIVE_BASE.straight(90)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(500, 300)
        await DRIVE_BASE.straight(-160)
        await DRIVE_BASE.turn(40)
        await DRIVE_BASE.straight(400)
        await DRIVE_BASE.straight(-300)
        await DRIVE_BASE.turn(-100)
        await DRIVE_BASE.straight(-700)
    
    DRIVE_BASE.use_gyro(False)    
    time2 = watch.time() 
    print(f"Time to finish: {time2 - time1} ms")


