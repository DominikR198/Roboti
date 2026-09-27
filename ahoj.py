from brian import motors
import brian.sensors as sn
motorP = motors.EV3LargeMotor(motors.MotorPort.C)
motorL = motors.EV3LargeMotor(motors.MotorPort.B)

color = sn.EV3.ColorSensorEV3(sn.SensorPort.S2)

motorP.wait_until_ready()
motorL.wait_until_ready()
#for i in range(4):
#
#    motorP.rotate_by_angle(-470, 360, 0)
#    motorL.rotate_by_angle(-470, 360)
#
#    motorP.rotate_by_angle(470, 360, 0)
#    motorL.rotate_by_angle(470, 360)

print(color.reflected_value())
