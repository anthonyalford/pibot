import threading
import time

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

# Based on code from
# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/using-dc-motors

DRIVE_DURATION = 0.050 # start with something small
ANGULAR_CONVERSION = 1.0 # not sure what to make this
MOVING_AVERAGE_FACTOR = 0.75 # for smoothing motor speed

class Drive (threading.Thread):

	def __init__(self, leftMotor, rightMotor):
		threading.Thread.__init__(self)
		self.keep_running = True
		self.leftMotor = leftMotor
		self.rightMotor = rightMotor
		self.g_lMS_old = 0.0
		self.g_rMS_old = 0.0
		self.speeds = [0.0, 0.0]

	def run(self):
		while self.keep_running:
			self.drive()
			time.sleep(0.001)

	def drive(self):

		fSpeed = self.speeds[0]
		aSpeed = self.speeds[1] * ANGULAR_CONVERSION

		lMS = int(MOVING_AVERAGE_FACTOR * self.g_lMS_old + (1.0 - MOVING_AVERAGE_FACTOR) * (fSpeed - aSpeed))
		self.g_lMS_old = lMS

		rMS = int(MOVING_AVERAGE_FACTOR * self.g_rMS_old + (1.0 - MOVING_AVERAGE_FACTOR) * (fSpeed + aSpeed))
		self.g_rMS_old = rMS

		self.leftMotor.run(Adafruit_MotorHAT.FORWARD)
		if abs(lMS) < 10:
			self.leftMotor.run(Adafruit_MotorHAT.RELEASE)
		elif lMS < 0:
			self.leftMotor.run(Adafruit_MotorHAT.BACKWARD)

		self.rightMotor.run(Adafruit_MotorHAT.FORWARD)
		if abs(rMS) < 10:
			self.rightMotor.run(Adafruit_MotorHAT.RELEASE)
		elif rMS < 0:
			self.rightMotor.run(Adafruit_MotorHAT.BACKWARD)

		self.leftMotor.setSpeed(abs(lMS))
		self.rightMotor.setSpeed(abs(rMS))
		time.sleep(DRIVE_DURATION)

		#leftMotor.run(Adafruit_MotorHAT.RELEASE)
		#rightMotor.run(Adafruit_MotorHAT.RELEASE)
