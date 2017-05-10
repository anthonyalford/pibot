import RPi.GPIO as GPIO

import threading
import time

# based on
# https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

MAX_SONAR_WAIT = 0.040 # corresponds to ~ 700 cm

class SonarArray (threading.Thread):

	def __init__(self, TRIG, ECHO_L, ECHO_C, ECHO_R):
		threading.Thread.__init__(self)
		self.keep_running = True
		self.ranges = [0.0,0.0,0.0]
		self.exitFlag = 0
		self.pins = [ECHO_L, ECHO_C, ECHO_R]
		self.TRIG = TRIG

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.TRIG,GPIO.OUT)
		GPIO.setup(ECHO_L,GPIO.IN)
		GPIO.setup(ECHO_C,GPIO.IN)
		GPIO.setup(ECHO_R,GPIO.IN)


	def run(self):
		while self.keep_running:
			self.ping()
			time.sleep(0.001)


	def ping(self):

		# need to send a 10us pulse to trigger pin
		GPIO.output(self.TRIG, False)
		time.sleep(0.01)
		GPIO.output(self.TRIG, True)				#Set TRIG as HIGH
		time.sleep(0.00001)					#Delay of 10 micro seconds
		GPIO.output(self.TRIG, False)			#Set TRIG as LOW

		# scan the sonars
		done = False
		loop_start = time.time()
		start_times = [loop_start, loop_start, loop_start]
		end_times = [loop_start, loop_start, loop_start]
		pulsed = [False, False, False]
		finished = [False, False, False]

		while done != True:
			for i in range(3):
				if finished[i]:
					continue

				if pulsed[i] != True:
					if GPIO.input(self.pins[i])==1:
						pulsed[i] = True
						start_times[i] = time.time()
				else:
					if GPIO.input(self.pins[i])==0:
						finished[i] = True
						end_times[i] = time.time()

			if time.time() - loop_start > MAX_SONAR_WAIT:
				done = True

		for i in range(3):
			self.ranges[i] = 17150.0 * (end_times[i] - start_times[i])
