# PI - Bot

Inspired by https://www.oreilly.com/learning/how-to-build-a-robot-that-sees-with-100-and-tensorflow

I built a robot using many of the components listed in that blog post.

The python code in this project includes
* Drive.py: a module for controlling the motors' speed
* SonarArray.py: a module for reading distance measurements from the sonar sensors
* Avoid.py: a module that implements an avoid obstacles behavior
* robot.py: a simple CLI for driving the robot

## Purchased parts
* [Raspberry Pi 3 Model B Motherboard ($40)](https://www.amazon.com/gp/product/B01CD5VC92/)
* [Adafruit DC & Stepper Motor HAT ($24)](https://www.amazon.com/gp/product/B00TIY5JM8)
* [GeauxRobot Raspberry Pi 3 B 2-layer Dog Bone Stack ($18)](https://www.amazon.com/gp/product/B00NU70MZS/)
* [INSMA Motor Smart Robot Car Chassis Kit ($17)](https://www.amazon.com/gp/product/B01BXPETQG/)
* [Arducam 5 Megapixels 1080p Camera ($15)](https://www.amazon.com/gp/product/B012V1HEP4)
* [Elegoo EL-CK-002 Electronic Fun Kit Bundle with Breadboard ($13)](https://www.amazon.com/gp/product/B01MRIG6YM/)
* [Elegoo HC-SR04 Sonar ($9)](https://www.amazon.com/gp/product/B01COSN7O6/)

Total: $136

## 3-D printed parts
* [Mounts for sonar](https://www.thingiverse.com/thing:2306533)
* [Mount for camera](https://www.thingiverse.com/thing:1637710)

## Setup
I didn't do a good job of writing down all the steps, but you should be able to find resources:
* [Installing an OS on the Pi](https://www.imore.com/how-get-started-using-raspberry-pi)
* [Installing camera drivers on the Pi](https://elinux.org/RPi-Cam-Web-Interface)
* [Installing Python package for the Motor Hat](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software)
* [Circuit and other info for sonars](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)



## Future Work
https://github.com/udacity/RoboND-Rover-Project
