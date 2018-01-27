from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import RPi.GPIO as GPIO
import sys
import time
import atexit
import readchar
import thread
from SonarArray import SonarArray
from Drive import Drive
from Avoid import Avoid

TRIG_R = 21
ECHO_R = 20
TRIG_C = 19
ECHO_C = 16
TRIG_L = 13
ECHO_L = 12


mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def cleanup():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
	GPIO.cleanup()


def main():
	atexit.register(cleanup)

	sonars = SonarArray(TRIG_L, TRIG_C, TRIG_R, ECHO_L, ECHO_C, ECHO_R)
	sonars.start()
	
	drive = Drive(mh.getMotor(1), mh.getMotor(3))
	drive.start()

	avoid = Avoid(sonars.ranges, drive.speeds)
	avoid.start()

	keep_running = True
	while keep_running:
		print str(sonars.ranges[0]) + "\t" + str(sonars.ranges[1]) + "\t" + str(sonars.ranges[2]) + \
			"\t" + str(drive.speeds[0]) + "\t" + str(drive.speeds[1])

		fs = 0
		angs = 0
		key = readchar.readkey()
		if key == 'w':
		  fs=150
		elif key == 'a':
		  angs=75
		elif key == 'd':
		  angs=-75
		elif key == 's':
		  fs=-75
		elif key == '~':
			keep_running = False
		else:
			fs=0
			angs=0

		avoid.commands[0] = fs
		avoid.commands[1] = angs

		time.sleep(0.1)

	print "Exiting...."

	sonars.keep_running = False
	drive.keep_running = False
	avoid.keep_running = False

if __name__ == "__main__":
	main()
