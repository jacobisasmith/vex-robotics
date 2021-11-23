import sys
import vex
import math

########################################################################################################################
#                                                                                                                      #
#                                               WALL-E Comp Version 0.5.4                                              #
#                                                                                                                      #
########################################################################################################################

# region config
brain = vex.Brain()
front_right_motor = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, True)
front_left_motor = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO18_1, False)
back_right_motor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, True)
back_left_motor = vex.Motor(vex.Ports.PORT20, vex.GearSetting.RATIO18_1, False)
fork_lift_motor = vex.Motor(vex.Ports.PORT9, vex.GearSetting.RATIO36_1, False)
DR4B_left_motor = vex.Motor(vex.Ports.PORT5, vex.GearSetting.RATIO36_1, False)
DR4B_right_motor = vex.Motor(vex.Ports.PORT6, vex.GearSetting.RATIO36_1, False)
index_motor = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO18_1, False)
con = vex.Controller(vex.ControllerType.PRIMARY)
# end region config

competition = vex.Competition()


def pre_auton():
    con.set_deadband(5)
    # Sets the Controller Deadband to 5 vex Percent Units
    sd = brain.sdcard.is_inserted()
    brain.screen.draw_eyes(vex.Eyes.BLUE_RESTING)
    # Draws Eyes on the Brain Screen
    if sd:
        print('SD Inserted')

    if not sd:
        print('SD NOT Inserted!')
    # Checks to see if an SD Card is Inserted into the brain


# PID Controller for Autonomous

# End PID Controller for Autonomous

# Functions for Autonomous
def brake_BRK():
    # Brakes with Brake Type Brake
    front_left_motor.stop(vex.BrakeType.BRAKE)
    back_left_motor.stop(vex.BrakeType.BRAKE)
    front_right_motor.stop(vex.BrakeType.BRAKE)
    back_right_motor.stop(vex.BrakeType.BRAKE)


def brake_CST():
    # Brakes with Brake Type Coast
    front_left_motor.stop(vex.BrakeType.COAST)
    back_left_motor.stop(vex.BrakeType.COAST)
    front_right_motor.stop(vex.BrakeType.COAST)
    back_right_motor.stop(vex.BrakeType.COAST)


def brake_HLD():
    # Brakes with Brake Type Hold
    front_left_motor.stop(vex.BrakeType.HOLD)
    back_left_motor.stop(vex.BrakeType.HOLD)
    front_right_motor.stop(vex.BrakeType.HOLD)
    back_right_motor.stop(vex.BrakeType.HOLD)


def turn_LFT(Time, Velocity):
    # Turns Left for Time + Velocity
    front_left_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    back_left_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    front_right_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    back_right_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    sys.sleep(float(Time))
    front_left_motor.stop()
    back_left_motor.stop()
    front_right_motor.stop()
    back_right_motor.stop()


def turn_RGT(Time, Velocity):
    # Turns Right for Time + Velocity
    front_left_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    back_left_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    front_right_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    back_right_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    sys.sleep(float(Time))
    front_left_motor.stop()
    back_left_motor.stop()
    front_right_motor.stop()
    back_right_motor.stop()


def strafe_LFT(Time, Velocity):
    # Strafes Left for Time + Velocity
    front_left_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    back_left_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    front_right_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    back_right_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    sys.sleep(float(Time))
    front_left_motor.stop()
    back_left_motor.stop()
    front_right_motor.stop()
    back_right_motor.stop()


def strafe_RGT(self, Time, Velocity):
    # Strafes Right for Time + Velocity
    front_left_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    back_left_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    front_right_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    back_right_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    sys.sleep(float(Time))
    front_left_motor.stop()
    back_left_motor.stop()
    front_right_motor.stop()
    back_right_motor.stop()


def strafe_DLFT(Time, Velocity):
    # Strafes Diagonoly Left for Time + Velocity
    front_left_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    back_right_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    sys.sleep(float(Time))
    front_left_motor.stop()
    back_right_motor.stop()


def strafe_DRGT(Time, Velocity):
    # Strafes Diagonoly Right for Time + Velocity
    back_left_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    front_right_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    sys.sleep(float(Time))
    back_left_motor.stop()
    front_right_motor.stop()


def DR4B_UP(Time, Velocity):
    # Moves DR4B Up for Time + Velocity
    DR4B_left_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    DR4B_right_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    sys.sleep(float(Time))
    DR4B_left_motor.stop()
    DR4B_right_motor.stop()


def DR4B_DWN(Time, Velocity):
    # Moves DR4B Down for Time + Velocity
    DR4B_left_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    DR4B_right_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    sys.sleep(float(Time))
    DR4B_left_motor.stop()
    DR4B_right_motor.stop()


def index_IN(self, Time, Velocity):
    # Inttakes for Time + Velocity
    index_motor.spin_for_time(vex.DirectionType.FWD, float(Time), vex.TimeUnits.SEC, float(Velocity),
                              vex.VelocityUnits.PCT)


def index_OUT(Time, Velocity):
    # Outtakes for Time + Velocity
    index_motor.spin_for_time(vex.DirectionType.FWD, float(Time), vex.TimeUnits.SEC, float(-Velocity),
                              vex.VelocityUnits.PCT)


def fork_UP(Time, Velocity):
    fork_lift_motor.spin_for_time(vex.DirectionType.FWD, float(Time), vex.TimeUnits.SEC, float(Velocity),
                                  vex.VelocityUnits.PCT)


def fork_DWN(Time, Velocity):
    # Moves Forklift Down for Time + Velocity
    fork_lift_motor.spin_for_time(vex.DirectionType.FWD, float(Time), vex.TimeUnits.SEC, float(-Velocity),
                                  vex.VelocityUnits.PCT)


def drive_FWD(Time, Velocity):
    # Drives Forward for Time + Velocity
    front_left_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    back_left_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    front_right_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    back_right_motor.spin(vex.DirectionType.FWD, float(Velocity), vex.VelocityUnits.PCT)
    sys.sleep(float(Time))
    front_left_motor.stop()
    back_left_motor.stop()
    front_right_motor.stop()
    back_right_motor.stop()


def drive_REV(Time, Velocity):
    # Drives Backward for Time + Velocity
    front_left_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    back_left_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    front_right_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    back_right_motor.spin(vex.DirectionType.FWD, float(-Velocity), vex.VelocityUnits.PCT)
    sys.sleep(float(Time))
    front_left_motor.stop()
    back_left_motor.stop()
    front_right_motor.stop()
    back_right_motor.stop()


def start():
    sys.run_in_thread(drive_FWD(1, 100))
    sys.run_in_thread(fork_UP(1, 100))


def end():
    sys.run_in_thread(fork_UP(1, 100))
    sys.run_in_thread(drive_FWD(1, 100))


# End Functions for Autonomous


def autonomous():
    start()
    drive_FWD(1, 100)
    end()


def drivercontrol():
    while True:
        # Sets Variables for Motor Power to Zero so that they can be changed later
        fork_lift_motor_power = 0
        DR4B_left_motor_power = 0
        DR4B_right_motor_power = 0
        index_motor_power = 0
        # Variable for Printing Eyes on Brain Screen
        a = 0

        # Checks to see if a button has been pressed if so changes the eyes on the brain to the angry variant else the eyes remain as the resting varient
        if a == 1:
            brain.screen.clear_screen()
            brain.screen.draw_eyes(vex.Eyes.BLUE_ANGRY)
        else:
            brain.screen.clear_screen()
            brain.screen.draw_eyes(vex.Eyes.BLUE_RESTING)

        if con.buttonL2.pressing():
            a = 1
            fork_lift_motor_power = 100

        if con.buttonL1.pressing():
            a = 1
            fork_lift_motor_power = -100

        if con.buttonR1.pressing():
            a = 1
            DR4B_left_motor_power = 100
            DR4B_right_motor_power = 100

        if con.buttonR2.pressing():
            a = 1
            DR4B_left_motor_power = -100
            DR4B_right_motor_power = -100

        if con.buttonUp.pressing():
            a = 1
            index_motor_power = 100

        if con.buttonDown.pressing():
            a = 1
            index_motor_power = -100

        fork_lift_motor.spin(vex.DirectionType.FWD, fork_lift_motor_power, vex.VelocityUnits.PCT)

        DR4B_left_motor.spin(vex.DirectionType.FWD, DR4B_left_motor_power, vex.VelocityUnits.PCT)
        DR4B_right_motor.spin(vex.DirectionType.FWD, DR4B_right_motor_power, vex.VelocityUnits.PCT)

        index_motor.spin(vex.DirectionType.FWD, index_motor_power, vex.VelocityUnits.PCT)

        front_left = (con.axis3.position(vex.PercentUnits.PCT) + con.axis4.position(
            vex.PercentUnits.PCT)) + con.axis1.position(vex.PercentUnits.PCT)
        back_left = (con.axis3.position(vex.PercentUnits.PCT) - con.axis4.position(
            vex.PercentUnits.PCT)) + con.axis1.position(vex.PercentUnits.PCT)
        front_right = (con.axis3.position(vex.PercentUnits.PCT) - con.axis4.position(
            vex.PercentUnits.PCT)) - con.axis1.position(vex.PercentUnits.PCT)
        back_right = (con.axis3.position(vex.PercentUnits.PCT) + con.axis4.position(
            vex.PercentUnits.PCT)) - con.axis1.position(vex.PercentUnits.PCT)

        max_raw_value = max(
            [math.fabs(front_left), math.fabs(back_left), math.fabs(front_right), math.fabs(back_right), 100])

        front_left = (float(front_left) / max_raw_value) * 100
        back_left = (float(back_left) / max_raw_value) * 100
        front_right = (float(front_right) / max_raw_value) * 100

        back_right = (float(back_right) / max_raw_value) * 100

        front_left_motor.spin(vex.DirectionType.FWD, front_left, vex.VelocityUnits.PCT)
        back_left_motor.spin(vex.DirectionType.FWD, back_left, vex.VelocityUnits.PCT)
        front_right_motor.spin(vex.DirectionType.FWD, front_right, vex.VelocityUnits.PCT)
        back_right_motor.spin(vex.DirectionType.FWD, back_right, vex.VelocityUnits.PCT)


competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)

pre_auton()
inertial_test()
