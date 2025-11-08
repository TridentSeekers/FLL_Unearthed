from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m3m4():
    SPEED = 550
    ACCELERATION = 350
    TURN_SPEED = 150
    TURN_ACCELERATION = 150
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)

    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)

    combined=0
    if (combined==1):
        DRIVE_BASE.reset_(angle=0)
        await DRIVE_BASE.turn(100)
        await DRIVE_BASE.straight(800)

    else:
        
        await DRIVE_BASE.straight(767)
        await DRIVE_BASE.turn(82)
        DRIVE_BASE.settings(straight_speed=100)
        DRIVE_BASE.settings(straight_acceleration=100)
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.straight(202)
        RIGHT_ATTACHMENT.reset_angle(0)
        await RIGHT_ATTACHMENT.run_target(900, 700)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(70, -30)
        await DRIVE_BASE.straight(-180)
        DRIVE_BASE.reset(distance=0, angle=0)
        watch = StopWatch()
        time1 = watch.time() 
        SPEED = 850
        ACCELERATION = 850
        TURN_SPEED = 550
        TURN_ACCELERATION = 550
        DRIVE_BASE.settings(straight_speed=SPEED)
        DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
        DRIVE_BASE.settings(turn_rate=TURN_SPEED)
        DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
        DRIVE_BASE.reset(distance=0, angle=0)
        await DRIVE_BASE.turn(-70)
        DRIVE_BASE.use_gyro(False)
        await DRIVE_BASE.straight(-800)
    
 
    time2 = watch.time() 
    print(f"Time to finish: {time2 - time1} ms")