from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from icon_library import REBEL, display_pulse_icon
from music_library import star_wars_opening
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

async def subtask():
    await display_pulse_icon(REBEL)
    # play some music to show off multitasking
    await star_wars_opening()

async def subtask2():
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(100)
    for count in range(10):
        await wait(0)
        await DRIVE_BASE.straight(300)
        await DRIVE_BASE.turn(180)
        await DRIVE_BASE.straight(300)
        await DRIVE_BASE.turn(-180)
    await DRIVE_BASE.straight(-100)
    DRIVE_BASE.use_gyro(False)

async def run1():
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