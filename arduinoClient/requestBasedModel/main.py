# request based model for arduino-pi communications
'''

#import arduino from client

ardFront = arduino("/dev/ttyACM0")
ardBack = arduino("/dev/ttyACM1")
#ardPow = arduino("/dev/ttyACM2")
time.sleep(.1)

# wait for ready signal from arduino
'''

# ardFront.begin()
# import logging
import asyncio

import serial
import time
import threading

from client import ardClient

# TODO: logging to file

# TODO: name these better

# time.sleep(2)

async def main():

	i = 0

	status = "NOT READY"

	ardFront = ardClient("/dev/ttyACM0")
	ardBack = ardClient("/dev/ttyACM1")

	await ardFront.waitToReady()
	await ardBack.waitToReady()

	time.sleep(2)

	ardFront.write("LED:ON")
	ardBack.write("LED:ON")

	while True:

		await asyncio.gather(ardFront.run(), ardBack.run())



print("endTest")

if __name__ == "__main__":

	s = time.perf_counter()
	asyncio.run(main())
	elapsed = time.perf_counter() - s
	print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# testing testing
