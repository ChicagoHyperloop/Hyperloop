# request based model for arduino-pi communications
'''

#import arduino from client

ardFront = arduino("/dev/ttyACM0")
ardBack = arduino("/dev/ttyACM1")
#ardPow = arduino("/dev/ttyACM2")
time.sleep(.1)

# wait for ready signal from arduino
'''

# ardFront.begin()
# import logging
import serial
import time
import threading

from client import ardClient

# TODO: logging to file

# TODO: name these better

# time.sleep(2)

i = 0

status = "NOT READY"

ardFront = ardClient("/dev/ttyACM0")
ardBack = ardClient("/dev/ttyACM1")

while True:

	data = ardFront.read()
	print("Front: " + data)

	if (data == "READY:"):
		time.sleep(1)
		ardFront.write("B:")
		break

while True:

	data = ardBack.read()
	print("Back: " + data)

	if (data == "READY:"):
		time.sleep(1)
		ardBack.write("B:")
		break

time.sleep(2)

ardFront.write("LED:ON")
ardBack.write("LED:ON")

while True:

	dataFront = ardFront.read()
	print("Front: " + dataFront)

	dataBack = ardBack.read()
	print("Back: " + dataBack)

	if dataFront == "LEDstat:OFF":
		time.sleep(1)
		ardFront.write("LED:ON")

	if dataBack == "LEDstat:OFF":
		time.sleep(1)
		ardBack.write("LED:ON")

print("endTest")

# testing testing
