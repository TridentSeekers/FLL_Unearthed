from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

#'Daniel', 'Luke', 'Joy','Aaron', 'Lincoln'
# Set the robot name to match the configuration in robot_config.py  
Robot_name = 'Daniel'
# Set up all devices.
# X: Positive means forward. Negative means backward.
# Y: Positive means to the left. Negative means to the right.
# Z: Positive means upward. Negative means downward.

if Robot_name == 'Daniel':
    HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    DRIVE_LEFT = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.D, Direction.CLOCKWISE)
    DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, wheel_diameter=61.4, axle_track=123) # Calibrated for Daniel
    # The axle track is the distance between the two drive wheels.
    LEFT_ATTACHMENT = Motor(Port.E, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.A, Direction.CLOCKWISE)
elif Robot_name == 'Luke':
    HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    DRIVE_LEFT = Motor(Port.D, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.E, Direction.CLOCKWISE)
    DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, wheel_diameter=61.3, axle_track=140)
    # The axle track is the distance between the two drive wheels.
    LEFT_ATTACHMENT = Motor(Port.C, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.A, Direction.CLOCKWISE)
elif Robot_name == 'Joy':
    HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    DRIVE_LEFT = Motor(Port.D, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.A, Direction.CLOCKWISE)
    DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, wheel_diameter=61.0, axle_track=125)
    # The axle track is the distance between the two drive wheels.
    LEFT_ATTACHMENT = Motor(Port.E, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.C, Direction.CLOCKWISE)
elif Robot_name == 'Aaron':
    HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    DRIVE_LEFT = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.C, Direction.CLOCKWISE)
    DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, wheel_diameter=61.3, axle_track=130)
    # The axle track is the distance between the two drive wheels.
    LEFT_ATTACHMENT = Motor(Port.F, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.D, Direction.CLOCKWISE)
elif Robot_name == 'Lincoln':
    HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    DRIVE_LEFT = Motor(Port.F, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.D, Direction.CLOCKWISE)
    DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, wheel_diameter=61.3, axle_track=130)
    # The axle track is the distance between the two drive wheels.
    LEFT_ATTACHMENT = Motor(Port.A, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.B, Direction.CLOCKWISE)
elif Robot_name == 'V':
    HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    DRIVE_LEFT = Motor(Port.F, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.D, Direction.CLOCKWISE)
    DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, wheel_diameter=61.3, axle_track=130)
    # The axle track is the distance between the two drive wheels.
    LEFT_ATTACHMENT = Motor(Port.A, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.B, Direction.CLOCKWISE)

# Initialize variables.
SPEED = 650
ACCELERATION = 650
TURN_SPEED = 150
TURN_ACCELERATION = 150
MANUAL_MOTOR_SPEED = 250 # Speed for manual motor control


