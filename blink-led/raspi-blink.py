#!/usr/bin/python
import RPi.GPIO as GPIO
import time

LED = 18

def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED, GPIO.OUT)
	
	while True:
		GPIO.output(LED, True)
		time.sleep(1)
		GPIO.output(LED, False)
		time.sleep(1)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
	finally:
		print "Interrupted, terminating."
		GPIO.cleanup
