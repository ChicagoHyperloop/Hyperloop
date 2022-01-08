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

class ardClient:

	def __init__(self, serialPath, baudRate = 9600, timeOut = .1, encoding = 'utf-8'):

		self.serialPort = serial.Serial(port=serialPath, baudrate=baudRate, timeout=timeOut)

		self.isReady = False
		self.baudRate = baudRate
		self.TIMEOUT = .1
		self.serialPath = serialPath
		self.encoding = encoding

	def setIsReady(self, isReady):
		self.isReady = isReady

	def setEncoding(self, encoding):
		self.encoding = encoding

	def write(self, data):

		self.serialPort.write(bytes(data, self.encoding))

	def read(self):

		thingRead = self.serialPort.readline().decode(self.encoding)

		size = len(thingRead)

		# remove line endings
		thingRead = thingRead[:size - 2]

		return thingRead

'''
def readingThreadFunc():

#	global timeMS

	while (True):

		print("read: " + read(arduino))

def writingThreadFunc():

	while (True):

		write(arduino, "Test")
		print("writing")
		time.sleep(.5)
'''

#TODO: name these better

#time.sleep(2)

i = 0

status = "NOT READY"

ardFront = ardClient("/dev/ttyACM0")

while (True) :

	data = ardFront.read()
	print(data)

	if (data == "READY:"):
		time.sleep(1)
		ardFront.write("B:")
		break

time.sleep(2)
ardFront.write("LED:ON")

while True:

	#data = input("send word ")
	#write(arduino, data)

	data = ardFront.read()
	print(data)

	if (data == "LEDstat:OFF"):
		time.sleep(1)
		ardFront.write("LED:ON")

	print(data)

print("endTest")

# testing testing

