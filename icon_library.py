from pybricks.tools import Matrix, multitask
from robot_config import HUB

async def display_pulse_icon(icon):
    # Create a list of intensities from 0 to 100 and back.
    brightness = list(range(0, 100, 4)) + list(range(100, 0, -4))
    HUB.display.animate([icon * i / 100 for i in brightness], 30)

async def display_icon(icon):
    HUB.display.icon(icon)

TRIDENT = Matrix(
    [
        [0, 0, 100, 0, 0],
        [100, 0, 100, 0, 100],
        [100, 100, 100, 100, 100],
        [0, 0, 100, 0, 0],
        [0, 0, 100, 0, 0],
    ]
)

REBEL = Matrix(
    [
        [0, 0, 100, 0, 0],
        [100, 0, 100, 0, 100],
        [100, 0, 100, 0, 100],
        [100, 100, 100, 100, 100],
        [0, 100, 100, 100, 0],
    ]
)

XWING = Matrix(
    [
        [0, 0, 100, 0, 0],
        [100, 0, 100, 0, 100],
        [100, 0, 100, 0, 100],
        [100, 100, 100, 100, 100],
        [0, 100, 0, 100, 0],
    ]
)

SMILE = Matrix(
    [
        [0, 100, 0, 100, 0],
        [0, 100, 0, 100, 0],
        [0, 0, 0, 0, 0],
        [100, 0, 0, 0, 100],
        [0, 100, 100, 100, 0],
    ]
)

CONCENTRATE = Matrix(
    [
        [0, 100, 0, 100, 0],
        [0, 100, 0, 100, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 100, 100],
        [1000, 100, 100, 100, 100],
    ]
)

WINK = Matrix(
    [
        [0, 100, 0, 0, 0],
        [0, 100, 0, 100, 100],
        [0, 0, 0, 0, 0],
        [100, 0, 0, 0, 100],
        [0, 100, 100, 100, 0],
    ]
)

WORRIED = Matrix(
    [
        [0, 0, 0, 0, 0],
        [100, 100, 0, 100, 100],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [100, 100, 100, 100, 100],
    ]
)

RIGHT_SMILE = Matrix(
    [
        [0, 0, 100, 0, 100],
        [0, 0, 100, 0, 100],
        [0, 0, 0, 0, 0],
        [100, 0, 0, 0, 100],
        [0, 100, 100, 100, 0],
    ]
)

LEFT_SMILE = Matrix(
    [
        [100, 0, 100, 0, 0],
        [100, 0, 100, 0, 0],
        [0, 0, 0, 0, 0],
        [100, 0, 0, 0, 100],
        [0, 100, 100, 100, 0],
    ]
)