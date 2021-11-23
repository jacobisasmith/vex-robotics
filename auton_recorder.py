import sys
import vex
import math

########################################################################################################################
#                                                                                                                      #
#                                           Autonomous Recorder Version 0.0.2                                          #
#                                                                                                                      #
########################################################################################################################

# Region Config
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
sd = brain.sdcard.is_inserted()


# End Region Config

def record():
    # rerunFile = open('/usd/rerun.txt', 'r')

    #if rerunFile:
        # usd_file_write = open('/usd/rerun.txt', 'w')
        # usd_file_write.write('')
        # usd_file_write.close()

    p1o = 0
    p11o = 0
    p10o = 0
    p20o = 0
    p9o = 0
    p5o = 0
    p6o = 0
    p4o = 0

    while True:

        p1n = front_right_motor.velocity(vex.VelocityUnits.PCT)
        p11n = front_left_motor.velocity(vex.VelocityUnits.PCT)
        p10n = back_right_motor.velocity(vex.VelocityUnits.PCT)
        p20n = back_left_motor.velocity(vex.VelocityUnits.PCT)
        p9n = fork_lift_motor.velocity(vex.VelocityUnits.PCT)
        p5n = DR4B_left_motor.velocity(vex.VelocityUnits.PCT)
        p6n = DR4B_right_motor.velocity(vex.VelocityUnits.PCT)
        p4n = index_motor.velocity(vex.VelocityUnits.PCT)

        if p1o != p1n:
            m1 = True

        if p11o != p11n:
            m11 = True

        if p10o != p10n:
            m10 = True

        if p20o != p20n:
            m20 = True

        if p9o != p9n:
            m9 = True

        if p5o != p5n:
            m5 = True

        if p6o != p6n:
            m6 = True

        if p4o != p4n:
            m4 = True

            # if rerunFile:
            # usd_file_write = open('/usd/rerun.txt', 'a')

            if m1:
                usd_file_write.write(
                    'front_right_motor.spin(vex.DirectionType.FWD, ' + p1n + ', vex.VelocityUnits.PCT) \n')
                p1n = p1o

            if m11:
                usd_file_write.write(
                    'front_left_motor.spin(vex.DirectionType.FWD, ' + p11n + ', vex.VelocityUnits.PCT) \n')
                p11n = p11o

            if m10:
                usd_file_write.write(
                    'back_right_motor.spin(vex.DirectionType.FWD, ' + p10n + ', vex.VelocityUnits.PCT) \n')
                p10n = p10o

            if m20:
                usd_file_write.write(
                    'back_left_motor.spin(vex.DirectionType.FWD, ' + p20n + ', vex.VelocityUnits.PCT) \n')
                p20n = p20o

            if m9:
                usd_file_write.write(
                    'fork_lift_motor.spin(vex.DirectionType.FWD, ' + p9n + ', vex.VelocityUnits.PCT) \n')
                p9n = p9o

            if m5:
                usd_file_write.write(
                    'DR4B_left_motor.spin(vex.DirectionType.FWD, ' + p5n + ', vex.VelocityUnits.PCT) \n')
                p5n = p5o

            if m6:
                usd_file_write.write(
                    'DR4B_right_motor.spin(vex.DirectionType.FWD, ' + p6n + ', vex.VelocityUnits.PCT) \n')
                p6n = p6o

            if m4:
                usd_file_write.write('index_motor.spin(vex.DirectionType.FWD, ' + p4n + ', vex.VelocityUnits.PCT) \n')
                p4n = p4o

            if not m1 or m11 or m10 or m20 or m9 or m5 or m6 or m4:
                usd_file_write.write('sys.sleep(' + tic - toc + ') \n')

            usd_file_write.close()

            sys.sleep(10)


while True:
    # rk_lift_motor_power = 0
    DR4B_left_motor_power = 0
    DR4B_right_motor_power = 0
    index_motor_power = 0
    # Variable  Sets Variables for Motor Power to Zero so that they can be changed later
    # for Printing Eyes on Brain Screen
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

    # fork_lift_motor.spin(vex.DirectionType.FWD, fork_lift_motor_power, vex.VelocityUnits.PCT)

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

    record()
