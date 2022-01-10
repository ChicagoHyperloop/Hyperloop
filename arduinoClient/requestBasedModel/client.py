import logging
import serial
import time
import asyncio
#import threading
#TODO: logging to file

class ardClient:

	def __init__(self, serialPath, baudRate=9600, timeOut=.1, encoding='utf-8'):

		self.logger = logging.getLogger('Hyperlogger')
		# self.comPort.flush()
		self.serialPort = serial.Serial(port=serialPath, baudrate=baudRate, timeout=timeOut)

		self.isReady = False
		self.baudRate = baudRate
		self.TIMEOUT = .1
		self.serialPath = serialPath
		self.encoding = encoding

		self.logger.info( "init" +
			"BAUD: " + str(self.baudRate) + " " +
			"TIMEOUT: " + str(self.TIMEOUT) + " " +
			"PATH: " + self.serialPath + " " +
			"Encoding: " + self.encoding + " ")

	def setIsReady(self, isReady):
		self.isReady = isReady

	def setEncoding(self, encoding):
		self.encoding = encoding

	def write(self, data):
		self.serialPort.write(bytes(data, self.encoding))
		self.logger.info("Sending " + self.serialPath + data)

	def read(self):
		data = self.serialPort.readline().decode(self.encoding)

		size = len(data)

		# remove line endings
		data = data[:size - 2]

		self.logger.info("read " + self.serialPath + "  "+ data)

		return data

	def sendCommand(self, prepend = "", data = ""):
		send = prepend + ":" + data
		self.write(send)
		print("sending: " + send)

	async def waitToReady(self):

		while True:

			data = self.read()
			print(self.serialPath + " :: " + data)

			if (data == "READY:"):

				self.sendCommand(prepend="B")
				break

			await asyncio.sleep(.1)

	async def run(self):

		data = self.read()
		print(self.serialPath + " :: " + data)

		if data == "LEDstat:OFF":
			await asyncio.sleep(.1)
			#self.write("LED:ON")
			self.sendCommand(prepend="LED", data="ON")

	# untested ------------------------------------------------------------------------------------>>>>

	def begin(self):
		self.sendCommand(prepend="B")

	def EStop(self):
		self.sendCommand(prepend="ES")

	def LEDchange(self):
		self.sendCommand(prepend="L")

	def basicSensorRefresh(self):
		self.sendCommand(prepend="S")
