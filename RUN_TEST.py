from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait, StopWatch
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT
from icon_library import display_pulse_icon, TRIDENT

# ROBOT is HUB
async def subtask():
    await display_pulse_icon(TRIDENT)


async def subtask2():
    await wait(0)
    # Just a demo to show off the drivebase as well as music, icons,
    # and multitasking
    # Turn button yellow; and beep/wait so hands are out of the way
    HUB.light.on(Color.YELLOW)
    DRIVE_BASE.use_gyro(True)
    timeout = StopWatch()
    while not HUB.imu.ready() and timeout.time() < 10000:
        wait(100)

    if not HUB.imu.ready():
        print("ERROR: IMU failed to initialize!")
        HUB.light.on(Color.RED)

    DRIVE_BASE.stop()
    DRIVE_BASE.reset(distance=0, angle=0)
    HUB.imu.reset_heading(0)
    Turn_ANGLE = 90
    await DRIVE_BASE.turn(Turn_ANGLE)
    await wait(1000)
    while True:
        yaw = HUB.imu.heading()
        print("Supposed to turn", Turn_ANGLE, "°.", f"Actual turned yaw: {yaw:.1f}°")
        wait(1000)
        break
    
    DRIVE_BASE.stop()
    DRIVE_BASE.reset(distance=0, angle=0)
    HUB.imu.reset_heading(0)
    Turn_ANGLE = -90
    await DRIVE_BASE.turn(Turn_ANGLE)
    await wait(1000)
    
    while True:
        yaw = HUB.imu.heading()
        print("Supposed to turn", Turn_ANGLE, "°.", f"Actual turned yaw: {yaw:.1f}°")
        wait(1000)
        break

    print("If actual turns are less than expected , increase robot_config.py axle_track=??.")
# Reset the drivebase and move forward
    print('Resetting drivebase and moving forward')
    DRIVE_BASE.stop()
    DRIVE_BASE.reset(distance=0, angle=0)
    Straight_DISTANCE = 300 #mm
    await DRIVE_BASE.straight(Straight_DISTANCE)
    while not DRIVE_BASE.done():
        await(10)
    print("Supposed to travel ", Straight_DISTANCE, " mm. Actual distance traveled", DRIVE_BASE.distance(), ' mm.')

    await wait(1000)

    print('Resetting drivebase and moving backward')
    DRIVE_BASE.stop()
    DRIVE_BASE.reset(distance=0, angle=0)
    Straight_DISTANCE = -300 #mm
    await DRIVE_BASE.straight(Straight_DISTANCE)
    while not DRIVE_BASE.done():
        await(10)
    print("Supposed to travel ", Straight_DISTANCE, " mm. Actual distance traveled", DRIVE_BASE.distance(), ' mm.')
    print("If actual distances are less than expected, decrease robot_config.py wheel_diameter=??.")
    DRIVE_BASE.use_gyro(False)

async def run_test():
    await wait(0)
    # Just a demo to show off the drivebase as well as music, icons,
    # and multitasking
    # Turn button yellow; and beep/wait so hands are out of the way
    HUB.light.on(Color.YELLOW)
    await HUB.speaker.beep(500, 400)
    await multitask(
        subtask(),
        subtask2(),
    )

async def main():
    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        wait(0),
    )


run_task(main())
