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

	global timeMS

	while True:
		thingRead = read(arduino)

		if (thingRead == "" or thingRead == "setup"):
			#print("slepRead")
			time.sleep(.05)
		else:
			print("read actual")
			timeMS = int(thingRead)
			print(thingRead)

#TODO: name these better

def reactiveFunc():

	global timeMS

	while True:

		ogTimeMS = timeMS

		timeMS = read(arduino)

		print("ard: ")
		print(timeMS)

		size = len(timeMS)

		if (timeMS == "setup"):
			timeMS = ogTimeMS
		if (size != 0 and type(timeMS) == str):
			#timeMS = timeMS[:size - 2]
			timeMS = int(timeMS)
		else:
			timeMS = ogTimeMS

		print("timeMS: ")
		print(timeMS)

		#print(timeMS)
		if (timeMS > 1500):
			print("write react")
			write(arduino, "L:1000")
			#to stop constant upload
			time.sleep(1)
		else:
			#print("slep react")
			time.sleep(.05)

#myReadThread = threading.Thread(target=readingThreadFunc, args = ())
#myReadThread.start()

myReactiveThread = threading.Thread(target=reactiveFunc, args = ())
myReactiveThread.start()

while True:
	time.sleep(.05)

print("endTest")
