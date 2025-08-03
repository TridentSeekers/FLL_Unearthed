from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

#'Daniel', 'Luke', 'Joy','Aaron', 'Lincoln'
# Set the robot name to match the configuration in robot_config.py  
Robot_name = 'Luke'
# Set up all devices.
# X: Positive means forward. Negative means backward.
# Y: Positive means to the left. Negative means to the right.
# Z: Positive means upward. Negative means downward.

if Robot_name == 'Daniel':
    HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    DRIVE_LEFT = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.D, Direction.CLOCKWISE)
    DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, wheel_diameter=61.3, axle_track=125) # Calibrated for Daniel
    # The axle track is the distance between the two drive wheels.
    LEFT_ATTACHMENT = Motor(Port.E, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.A, Direction.CLOCKWISE)
elif Robot_name == 'Luke':
    HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    DRIVE_LEFT = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    DRIVE_RIGHT = Motor(Port.D, Direction.CLOCKWISE)
    DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, wheel_diameter=61.3, axle_track=120)
    # The axle track is the distance between the two drive wheels.
    LEFT_ATTACHMENT = Motor(Port.C, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.E, Direction.CLOCKWISE)
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
    LEFT_ATTACHMENT = Motor(Port.B, Direction.CLOCKWISE)
    RIGHT_ATTACHMENT = Motor(Port.A, Direction.CLOCKWISE)


# Initialize variables.
SPEED = 620
ACCELERATION = 600
TURN_SPEED = 400
TURN_ACCELERATION = 500
MANUAL_MOTOR_SPEED = 250



# The main program starts here.
# This is where you configure all the variables as well as
# the parts of the robot. These values are then imported/used as necessary.

# Change to match the setup of your robot. Adjust speeds as necessary
