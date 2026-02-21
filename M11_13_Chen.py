from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m11_13():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    SPEED = 450
    ACCELERATION = 450
    TURN_SPEED = 200
    TURN_ACCELERATION = 250
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    watch = StopWatch()
    time1 = watch.time()

    #await DRIVE_BASE.turn(5)
    await DRIVE_BASE.straight(825) #815
    await DRIVE_BASE.turn(-68) #it was -72
    DRIVE_BASE.reset(angle=0)
    # goes to mission
    DRIVE_BASE.use_gyro(False)
    await DRIVE_BASE.straight(175) #195 #190 #180
    DRIVE_BASE.reset(angle=0)
    # meets the funnel and it turns right
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.turn(-11) #-16 #-14    #it was -27
    DRIVE_BASE.reset(angle=0)
    # await DRIVE_BASE.straight(200) #it was commented
    # # await DRIVE_BASE.turn(10)
    LEFT_ATTACHMENT.reset_angle(0)
    await LEFT_ATTACHMENT.run_target(250, -1000)
    await DRIVE_BASE.turn(5) #10 #5
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.straight(-150)
    # goes to mission
    # SPEED = 450
    # ACCELERATION = 650
    # TURN_SPEED = 250
    # TURN_ACCELERATION = 200
    # DRIVE_BASE.settings(straight_speed=SPEED)
    # DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    # DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    # DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    # DRIVE_BASE.reset(distance=0, angle=0)

    RIGHT_ATTACHMENT.reset_angle(0)
    await multitask(RIGHT_ATTACHMENT.run_target(1000,-1000),DRIVE_BASE.turn(123)) #121 #124
    DRIVE_BASE.reset(angle=0)
    await DRIVE_BASE.straight(285) #310 #300
   
    # RIGHT_ATTACHMENT.reset_angle(0)
    # # await multitask(RIGHT_ATTACHMENT.run_target(600,500),DRIVE_BASE.turn(40))
    await RIGHT_ATTACHMENT.run_target(850,200)
    SPEED = 450
    ACCELERATION = 650
    TURN_SPEED = 350
    TURN_ACCELERATION = 450
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.turn(43) #35 #38 #40
    SPEED = 1000
    ACCELERATION = 1000
    TURN_SPEED = 750
    TURN_ACCELERATION = 650
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    await DRIVE_BASE.straight(-90)
    await DRIVE_BASE.turn(82) #90
    DRIVE_BASE.use_gyro(False)
    await DRIVE_BASE.straight(-850)

    time2 = watch.time() 
    print(f"Time to finish: {time2 - time1} ms")