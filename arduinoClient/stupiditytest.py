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


#testing testing

def writingThreadFunc():

	while (True):

		write(arduino, "Test")
		print("writing")
		time.sleep(.5)




'''
	while True:
		thingRead = read(arduino)

		if (thingRead == "" or thingRead == "setup"):
			#print("slepRead")
			time.sleep(.05)
		else:
			print("read actual")
			timeMS = int(thingRead)
			print(thingRead)

'''

#TODO: name these better

'''
	while True:

		if (timeMS > 1500):
			print("write react")
			write(arduino, "L:1000")
			#to stop constant upload
			time.sleep(1)
		else:
			print("slep react")
			time.sleep(.05)
'''
'''
myWritingThread = threading.Thread(target=writingThreadFunc, args = ())
myWritingThread.start()

myReadThread = threading.Thread(target=readingThreadFunc, args = ())
myReadThread.start()

#myReactiveThread = threading.Thread(target=reactiveFunc, args = ())
#myReactiveThread.start()
'''

time.sleep(2)
i = 0

while True:

	data = input("send word ")
	write(arduino, data)

	while i < 50:
		print(read(arduino))
		i += 1

	i = 0

print("endTest")

# testing testing

