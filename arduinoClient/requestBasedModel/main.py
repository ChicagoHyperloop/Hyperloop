#request based model for arduino-pi communications
import time
from client import arduino
#import arduino from client

ardFront = arduino("/dev/ttyACM0")
ardBack = arduino("/dev/ttyACM1")
#ardPow = arduino("/dev/ttyACM2")
time.sleep(.1)

# wait for ready signal from arduino
'''
while (True):
	read = ardFront.read()
	print("Rear sends:            " + read)

	if (read == "Ready1:" or read == "Ready2:"):
		time.sleep(.1)
		break;
'''
#ardFront.begin()
ardFront.begin()
time.sleep(.1)

isRunning = True

while (isRunning):

	#ardBack.basicSensorRefresh()

	#time.sleep(.1)

	dataBack = ardFront.read()

	print("Rear sends:     " + dataBack)

#	print("waiting for data")

#	while (dataBack == ""):
	'''
		newReadFront = ardFront.read()
		print("Front:     " + dataFront)

		if (newReadFront != "" and dataFront == ""):

			print("dataFront = " + newReadFront)
			dataFront = newReadFront
		
		newReadBack = ardBack.read()
		print("Rear sends:       " + dataBack)

		if (newReadBack != "" and dataBack == ""):
			print("dataBack = " + newReadBack)
			dataBack = newReadBack
	'''
	#print("loop reset")
