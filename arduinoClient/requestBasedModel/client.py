#import logging
import serial
import time
#import threading
#TODO: logging to file

class ardClient:

	def __init__(self, serialPath, baudRate=9600, timeOut=.1, encoding='utf-8'):
		self.serialPort = serial.Serial(port=serialPath, baudrate=baudRate, timeout=timeOut)

		self.isReady = False
		self.baudRate = baudRate
		self.TIMEOUT = .1
		self.serialPath = serialPath
		self.encoding = encoding

	# self.comPort.flush()

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

	# untested ------------------------------------------------------------------------------------>>>>
	def sendCommand(self, prepend = "", data = ""):
		send = prepend + ":" + data
		self.write(send)
		print("sending: " + send)

	def begin(self):
		self.sendCommand(prepend="B")

	def EStop(self):
		self.sendCommand(prepend="ES")

	def LEDchange(self):
		self.sendCommand(prepend="L")

	def basicSensorRefresh(self):
		self.sendCommand(prepend="S")
