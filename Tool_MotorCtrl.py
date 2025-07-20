# -----------------------------------------------------------------------------
# Tool - Motor Control Tester for LEGO SPIKE Prime (Pybricks)
#
# Description:
#   Allows the user to select motors on ports A–F.
#   Controls motor rotation direction (forward, reverse, stop) via buttons.
#   Displays the selected motor port and rotation status on the hub screen.
#
#   - Left/Right Button: Port selection and FWD/RWD control
#   - Center Button    : Toggle between Port Selection and Motor Control modes
#   - Bluetooth Button : Stop the program
#
# Author  : Anthony Hsu - OFDL Taiwan https://github.com/ofdl-robotics-tw
# Date    : 2025/05/23, Ver 1.0
# Platform: LEGO SPIKE Prime (Pybricks)
# -----------------------------------------------------------------------------
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor as _Motor, DCMotor as _DCMotor
from pybricks.parameters import Button, Direction, Port, Icon
from pybricks.tools import hub_menu, wait

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

motorA = Motor(Port.A)
motorB = Motor(Port.B)
motorC = Motor(Port.C)
motorD = Motor(Port.D)
motorE = Motor(Port.E)
motorF = Motor(Port.F)
hub = PrimeHub()
hub.speaker.volume(50)
hub.system.set_stop_button(Button.BLUETOOTH)

iconFWD = Icon(4657152)
iconRWD = Icon(458752)
iconNOD = Icon(0)

def MotorCtrl():
    motorID = 1
    motorList = ["_" ,"A", "B", "C", "D", "E", "F"]
    motorDotPosX = [0, 0, 0, 2, 2, 4, 4]
    motorDotPosY = [0 ,0, 4, 0, 4, 0, 4]
    motorMap = {
        1: motorA,
        2: motorB,
        3: motorC,
        4: motorD,
        5: motorE,
        6: motorF
    }
    while True:
        btn = hub.buttons.pressed()
        hub.display.char(motorList[motorID])
        if (Button.LEFT in btn):
            hub.speaker.beep(440, 180)
            if (motorID > 1): motorID = motorID - 1
        elif (Button.RIGHT in btn):
            hub.speaker.beep(440, 180)
            if (motorID < 6): motorID = motorID + 1
        elif (Button.CENTER in btn):
            hub.speaker.beep(540, 180)
            hub.display.off()
            wait(200)
            while not (Button.CENTER in hub.buttons.pressed()):
                btn = hub.buttons.pressed()
                if (Button.LEFT in btn): 
                    motorMap[motorID].dc(-100)
                    hub.display.icon(iconRWD)
                elif (Button.RIGHT in btn): 
                    motorMap[motorID].dc(100)
                    hub.display.icon(iconFWD)
                else: 
                    motorMap[motorID].dc(0)
                    hub.display.icon(iconNOD)
                hub.display.pixel(motorDotPosX[motorID],  motorDotPosY[motorID])
            hub.display.off()
            wait(200)

MotorCtrl()