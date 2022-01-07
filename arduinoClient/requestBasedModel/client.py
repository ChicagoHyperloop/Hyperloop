#import logging
import serial
import time
#import threading
#TODO: logging to file

class arduino:

	def __init__(self, path, encoding = 'utf-8', baud = 9600, TIMEOUT = .1):

		self.comPort = serial.Serial(port = path, baudrate = baud, timeout = TIMEOUT)

		self.path = path
		self.encoding = encoding
		self.baud = baud
		self.timeout = TIMEOUT

		self.comPort.flush()

	def write (self, data):

		self.comPort.write(bytes(data, self.encoding))

	def read (self):

		#global timeMS
		thingRead = self.comPort.readline().decode(self.encoding)

		# remove line endings
		size = len(thingRead)
		thingRead = thingRead[:size - 2]

		return thingRead


	def sendCommand(self, prepend = "", data = ""):
		send = prepend + ":" + data
		self.write(send)
		print("sending: " + send)

	def begin(self):
		self.sendCommand(prepend = "B")

	def EStop(self):
		self.sendCommand(prepend = "ES")

	def LEDchange(self):
		self.sendCommand(prepend = "L")

	def basicSensorRefresh(self):
		self.sendCommand(prepend = "S")
