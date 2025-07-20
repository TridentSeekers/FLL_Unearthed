# -----------------------------------------------------------------------------
# Tool - Motor RPM Test Program for LEGO SPIKE Prime (Pybricks)
#
# Description:
#   Real-time preview of motor RPMs for two ports.
#   Ensures consistent loop timing to achieve high-precision RPM readings.
#
# Author  : Anthony Hsu - OFDL Taiwan https://github.com/ofdl-robotics-tw
# Date    : 2025/05/23, Ver 1.1
# Platform: LEGO SPIKE Prime (Pybricks)
# -----------------------------------------------------------------------------
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor as _Motor, DCMotor as _DCMotor
from pybricks.parameters import Button, Direction, Port
from pybricks.tools import wait, StopWatch


Robot_name = 'Joy'


# ---------- Begin Allow Missing Motors ----------
def do_nothing(*args, **kwargs):
    return 0

class NoneMotor:
    def __getattr__(self, name):
        return do_nothing

class AnyDCMotor(_DCMotor):
    def __getattr__(self, name):
        return do_nothing

def Motor(port, direction=Direction.CLOCKWISE):
    try:
        return _Motor(port, direction)
    except OSError:
        try:
            return AnyDCMotor(port, direction)
        except OSError:
            return NoneMotor()

DCMotor = Motor
# ---------- End Allow Missing Motors ----------
hub = PrimeHub()
if Robot_name == 'Daniel':
    DRIVE_LEFT = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.D, Direction.CLOCKWISE)
    LEFT_ATTACHMENT = Motor(Port.E, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.A, Direction.CLOCKWISE)
elif Robot_name == 'Luke':
    DRIVE_LEFT = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.D, Direction.CLOCKWISE)
    LEFT_ATTACHMENT = Motor(Port.C, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.E, Direction.CLOCKWISE)
elif Robot_name == 'Joy':
    DRIVE_LEFT = Motor(Port.D, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.A, Direction.CLOCKWISE)
    LEFT_ATTACHMENT = Motor(Port.E, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.C, Direction.CLOCKWISE)

motorLeft = DRIVE_LEFT
motorRight = DRIVE_RIGHT
timer = StopWatch()

buf_left = 0
buf_right = 0
buf_t = 0
last_left = 0
last_right = 0
last_t = 0
chg_left = 0
chg_right = 0
chg_t = 0
diff = 0
t = 500
conv = 0

motorLeft.dc(100)
motorRight.dc(100)
timer.reset()
while True:
    buf_left = motorLeft.angle()
    buf_right = motorRight.angle()

    chg_left = buf_left - last_left
    chg_right = buf_right - last_right

    last_left = buf_left
    last_right = buf_right

    buf_t = timer.time()
    chg_t = buf_t - last_t
    while chg_t < t:
        buf_t = timer.time()
        chg_t = buf_t - last_t
    last_t = buf_t

    conv = 60 * (1000 / chg_t) / 360
    diff = chg_left - chg_right

    print(f"RPM L: {chg_left*conv:5.1f}, R: {chg_right*conv:5.1f}, DIFF: {diff*conv:5.1f}, Loop T: {chg_t}")

