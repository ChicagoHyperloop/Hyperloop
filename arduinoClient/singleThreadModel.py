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

#TODO: name these better


# the difference is that the reads are conducted inside of the looping thread
# meaning we might be able to remove the complex threading later if this works,
# i do an expiriment next
# to see if the read func will extract old inputs as well

def reactiveFunc():

	global timeMS

	write(arduino, "L:500")

	t = 0

	while t <= 60:


		#write(arduino, "L:1000")

		#arduinoRead =  read(arduino)

		#print("current arduino stuff at t = 0")
		#print(arduinoRead)

		#time.sleep(10)

		arduinoRead = read(arduino)

		print("arduino Read at t = ")
		print(t)
		print(arduinoRead)

		t +=10

		time.sleep(10)

	print("t > 60  full dump")

	while True:

		arduinoRead = read(arduino)

		print(arduinoRead)
'''

	while True:

		# ik there a better way to do this but it doesnt rly matter atm
		ogTimeMS = timeMS

		timeMS = read(arduino)

		print("ard: ")
		print(timeMS)

		size = len(timeMS)

		if (timeMS == "setup"):
			timeMS = ogTimeMS
		elif (size != 0 and type(timeMS) == str):
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
'''

myReactiveThread = threading.Thread(target=reactiveFunc, args = ())
myReactiveThread.start()

while True:
	time.sleep(.5)

print("endTest")
