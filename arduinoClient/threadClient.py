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
	global timeMS

	thingRead = arduinoToRead.readline().decode(encoding)

	size = len(thingRead)
	thingRead = thingRead[:size - 2]

	if (thingRead != "" and thingRead != "setup"):
		timeMS = int(thingRead)

	return thingRead

def readingThreadFunc():

	while True:
		thingRead = read(arduino)

		if (thingRead == ""):
			#print("slepRead")
			time.sleep(.05)
			pass
		else:
			print("read actual")
			timeMS = thingRead
			print(thingRead)

#TODO: name these better
def reactiveFunc():
	while True:
		print(timeMS)
		if (timeMS > 1500):
			print("write react")
			write(arduino, "L:1000")
		else:
			#print("slep react")
			time.sleep(.05)

myReadThread = threading.Thread(target=readingThreadFunc, args =())
myReadThread.start()

myReactiveThread = threading.Thread(target=reactiveFunc, args=())
myReactiveThread.start()

while True:
	time.sleep(.05)

print("endTest")
