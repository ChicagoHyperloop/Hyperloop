#request based model for arduino-pi communications
'''
import time
from client import arduino
#import arduino from client

ardFront = arduino("/dev/ttyACM0")
ardBack = arduino("/dev/ttyACM1")
#ardPow = arduino("/dev/ttyACM2")
time.sleep(.1)

# wait for ready signal from arduino
'''

#ardFront.begin()
#import logging
import serial
import time
import threading
#TODO: logging to file

arduino = serial.Serial(port = "/dev/ttyACM0", baudrate = 9600, timeout = .1)

encoding = 'utf-8'

timeMS = -1

def write (arduinoToWrite, data):

	arduinoToWrite.write(bytes(data, encoding))
	time.sleep(.05)

def read (arduinoToRead):
	#global timeMS

	thingRead = arduinoToRead.readline().decode(encoding)

	size = len(thingRead)

	#remove line endings
	thingRead = thingRead[:size - 2]

	return thingRead

def readingThreadFunc():

#	global timeMS

	while (True):

		print("read: " + read(arduino))

def writingThreadFunc():

	while (True):

		write(arduino, "Test")
		print("writing")
		time.sleep(.5)

#TODO: name these better

#time.sleep(2)
i = 0

status = "NOT READY"
while (True) :

	data = read(arduino)
	print(data)

	if (data == "READY:"):
		time.sleep(1)
		write(arduino, "B:")
		break

time.sleep(2)
write(arduino, "LED:ON")

while True:

	#data = input("send word ")
	#write(arduino, data)

	data = read(arduino)
	print(data)

	if (data == "LEDstat:OFF"):
		time.sleep(1)
		write(arduino, "LED:ON");

	print(data)

print("endTest")

# testing testing

