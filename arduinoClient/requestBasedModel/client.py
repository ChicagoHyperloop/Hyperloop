'''
this file contains the ardClient class
which has stuff necessary for communicating with arduino
and arduino methods and Command stuff
'''

import logging
import serial
import asyncio
import json

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

		send = prepend + ":" + data + ";"
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


	def JSONExpirement(self):

		commandDict = {

			"tempLeft":50,
			"tempRight":53.2

		}

		print(json.dump(fp=self,obj=commandDict))

		'''
		data = self.read()
		self.sendCommand(prepend="GETTEMP")
		while True:
			data = self.read()

			if "TEMPstat" in data:
				break

		size = len(data)
		# remove semicolon
		data = data[:size - 1]

		listData = data.split(':')
		return [listData[1], listData[2]]
		'''

	# untested ------------------------------------------------------------------------------------>>>>

	def begin(self):
		self.sendCommand(prepend="B")

	def EStop(self):
		self.sendCommand(prepend="ES")

