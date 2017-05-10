import threading
import time

FRONT_SPRING_RANGE = 75
FRONT_SPRING_CONSTANT = 1.0

SIDE_SPRING_RANGE = 75
SIDE_SPRING_CONSTANT = 1.0

class Avoid (threading.Thread):

	def __init__(self, ranges, speeds):
		threading.Thread.__init__(self)
		self.keep_running = True
		self.ranges = ranges
		self.speeds = speeds
		self.commands = [0.0, 0.0]


	def run(self):
		while self.keep_running:
			self.avoid_inverse()
			time.sleep(0.001)


	def avoid_spring(self):
		left = self.ranges[0]
		center = self.ranges[1]
		right = self.ranges[2]

		fs = self.commands[0]
		angs = self.commands[1]

		if center > 0 and center < FRONT_SPRING_RANGE:
			fs = fs - FRONT_SPRING_CONSTANT * (FRONT_SPRING_RANGE - center)

		if left > 0 and left < SIDE_SPRING_RANGE:
			angs = angs - SIDE_SPRING_CONSTANT * (SIDE_SPRING_RANGE - left)

		if right > 0 and right < 50:
			angs = angs + SIDE_SPRING_CONSTANT * (SIDE_SPRING_RANGE - right)

		self.speeds[0] = fs
		self.speeds[1] = angs


	def avoid_inverse(self):
		left = self.ranges[0]
		center = self.ranges[1]
		right = self.ranges[2]

		fs = self.commands[0]
		angs = self.commands[1]

		if center > 0 and center < FRONT_SPRING_RANGE:
			fs = fs -( FRONT_SPRING_RANGE + int( 150.0 / center ))

		# hard limit
		if center > 0 and center < 10:
			fs = min(fs, 0)

		if left > 0 and left < SIDE_SPRING_RANGE:
			angs = angs - (25 + int( 100.0 / left ))

		if right > 0 and right < SIDE_SPRING_RANGE:
			angs = angs + (25 + int( 100.0 / right ))

		self.speeds[0] = fs
		self.speeds[1] = angs
