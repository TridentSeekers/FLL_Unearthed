from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def m11_13():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    SPEED = 450
    ACCELERATION = 650
    TURN_SPEED = 450
    TURN_ACCELERATION = 650
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    DRIVE_BASE.use_gyro(True)
    watch = StopWatch()
    time1 = watch.time()

    await DRIVE_BASE.straight(820)
    await DRIVE_BASE.turn(-60)
    await DRIVE_BASE.straight(95)
    await DRIVE_BASE.turn(-35)
    LEFT_ATTACHMENT.reset_angle(0)
    await LEFT_ATTACHMENT.run_target(1000, -800)
    await DRIVE_BASE.turn(20)
    
    await DRIVE_BASE.straight(-110)
    RIGHT_ATTACHMENT.reset_angle(0)
    await multitask(RIGHT_ATTACHMENT.run_target(1000,-800),DRIVE_BASE.turn(120))
    await DRIVE_BASE.straight(350)
   
    RIGHT_ATTACHMENT.reset_angle(0)
    # await multitask(RIGHT_ATTACHMENT.run_target(600,500),DRIVE_BASE.turn(40))
    await RIGHT_ATTACHMENT.run_target(600,600)
    await DRIVE_BASE.turn(40)
    SPEED = 850
    ACCELERATION = 850
    TURN_SPEED = 550
    TURN_ACCELERATION = 550
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
    DRIVE_BASE.reset(distance=0, angle=0)
    await DRIVE_BASE.straight(-100)
    await DRIVE_BASE.turn(80)
    await DRIVE_BASE.straight(-600)
    DRIVE_BASE.use_gyro(False)
    time2 = watch.time() 
    print(f"Time to finish: {time2 - time1} ms")