from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m1m2():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    SPEED = 850
    ACCELERATION = 850
    TURN_SPEED = 550
    TURN_ACCELERATION = 550
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
        await RIGHT_ATTACHMENT.run_angle(200, -250)
        await DRIVE_BASE.straight(-200)
        DRIVE_BASE.reset(angle=0)
        await DRIVE_BASE.turn(-30)
        await DRIVE_BASE.straight(75)
        LEFT_ATTACHMENT.reset_angle(0)
        await LEFT_ATTACHMENT.run_target(100, -70)
        
        await DRIVE_BASE.curve(-260,-160)
        DRIVE_BASE.use_gyro(False)
        # DRIVE_BASE.reset(distance=0, angle=0)
        # await DRIVE_BASE.turn(150)
        # await DRIVE_BASE.straight(-150)

    time2 = watch.time() 
    print(f"Time to finish: {time2 - time1} ms")
