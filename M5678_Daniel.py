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
    ACCELERATION = 500
    TURN_SPEED = 200
    TURN_ACCELERATION = 180
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    watch = StopWatch()
    time1 = watch.time() 
    combined=0
    if (combined ==1):
        await DRIVE_BASE.straight(400)   
        # Finish three times silo
        for i in range(2):
            LEFT_ATTACHMENT.reset_angle(0) #need
            await LEFT_ATTACHMENT.run_target(1200,130)
            wait(200)            
            LEFT_ATTACHMENT.reset_angle(0) #need
            await LEFT_ATTACHMENT.run_target(1000,-130)
        LEFT_ATTACHMENT.reset_angle(0) #need
        await LEFT_ATTACHMENT.run_target(1200,130)
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.turn(-90)
        # Go to M5
        await DRIVE_BASE.straight(180)
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.turn(93)
        await DRIVE_BASE.straight(355)
        # Turn left to finish M5
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.turn(-56)
        LEFT_ATTACHMENT.reset_angle(0)
        await multitask(LEFT_ATTACHMENT.run_target(600, -150),DRIVE_BASE.turn(57))
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.straight(49)

        await DRIVE_BASE.turn(55)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(300, -130)
        await DRIVE_BASE.turn(90)   
        # DRIVE_BASE.reset(distance=0, angle=0)
        # await DRIVE_BASE.straight(37)
        # RIGHT_ATTACHMENT.reset_angle(0)
        # await RIGHT_ATTACHMENT.run_target(400, 150)
        # DRIVE_BASE.reset(distance=0, angle=0)
        # await DRIVE_BASE.straight(-145)
        # await DRIVE_BASE.turn(39)
        # await DRIVE_BASE.straight(420)
        # await DRIVE_BASE.straight(-270)
        # SPEED = 850
        # ACCELERATION = 850
        # TURN_SPEED = 550
        # TURN_ACCELERATION = 550
        # DRIVE_BASE.settings(straight_speed=SPEED)
        # DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
        # DRIVE_BASE.settings(turn_rate=TURN_SPEED)
        # DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
        # DRIVE_BASE.reset(distance=0, angle=0)
        # await DRIVE_BASE.turn(-100)
        # await DRIVE_BASE.straight(-650)
    else:
        await DRIVE_BASE.straight(402)   
        # Finish three times silo
        for i in range(2):
            LEFT_ATTACHMENT.reset_angle(0) #need
            await LEFT_ATTACHMENT.run_target(1200,130)
            wait(200)            
            LEFT_ATTACHMENT.reset_angle(0) #need
            await LEFT_ATTACHMENT.run_target(1000,-130)
        LEFT_ATTACHMENT.reset_angle(0) #need
        await LEFT_ATTACHMENT.run_target(1200,130)
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.turn(-90)
        # Go to M5
        await DRIVE_BASE.straight(180)
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.turn(92)
        await DRIVE_BASE.straight(346)
        # Turn left to finish M5
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.turn(-24)
        await DRIVE_BASE.straight(-5)
        LEFT_ATTACHMENT.reset_angle(0)
        await multitask(LEFT_ATTACHMENT.run_target(600, -250),DRIVE_BASE.turn(30))
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.straight(25)
        await DRIVE_BASE.turn(40)
        
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(1000, -150)
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.straight(45)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(500, 300)
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.straight(-170)
        await DRIVE_BASE.turn(42)

        SPEED = 850
        ACCELERATION = 850
        TURN_SPEED = 550
        TURN_ACCELERATION = 550
        DRIVE_BASE.settings(straight_speed=SPEED)
        DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
        DRIVE_BASE.settings(turn_rate=TURN_SPEED)
        DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.straight(420)
        await DRIVE_BASE.straight(-330)
        await DRIVE_BASE.turn(-92)
        await DRIVE_BASE.straight(-650)
    
    DRIVE_BASE.use_gyro(False)    
    time2 = watch.time() 
    print(f"Time to finish: {time2 - time1} ms")


