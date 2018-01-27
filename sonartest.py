import RPi.GPIO as GPIO
import sys
import time
import atexit
import readchar
import thread
from SonarArray import SonarArray

TRIG_R = 21
ECHO_R = 20
TRIG_C = 19
ECHO_C = 16
TRIG_L = 13
ECHO_L = 12


# recommended for auto-disabling motors on shutdown!
def cleanup():
	GPIO.cleanup()


def main():
	atexit.register(cleanup)
	GPIO.setmode(GPIO.BCM)


	sonars = SonarArray(TRIG_L, TRIG_C, TRIG_R, ECHO_L, ECHO_C, ECHO_R)
	sonars.start()


	keep_running = True
	while keep_running:
		print str(sonars.ranges[0]) + "\t" +  str(sonars.ranges[1]) + "\t" + str(sonars.ranges[2])
		key = readchar.readkey()
		if key == '~':
			keep_running = False
		else:
			fs=0
			angs=0

		time.sleep(0.1)

	print "Exiting...."

	sonars.keep_running = False

if __name__ == "__main__":
	main()
