'''
main file for all code on the raspberry pi
developed on:
	rpi nano,
	windows Pycharm ssh into rpi,
	windows WSLS ssh into rpi nano,
	and Ubuntu ssh into rpi nano

developed by: Everyone except Carl

'''
import sys
import logging
import asyncio
import time
from client import ardClient

async def main():

	ardFront = ardClient("/dev/ttyACM0")
	ardBack = ardClient("/dev/ttyACM1")

	await asyncio.gather(ardFront.waitToReady(), ardBack.waitToReady())

	time.sleep(2)

	ardFront.getTemp()

	time.sleep(2)

	#ardFront.write("LED:ON")
	#ardBack.write("LED:ON")

	while True:

		await asyncio.gather(ardFront.run(), ardBack.run())

if __name__ == "__main__":

	logFilePath = "../../logs/" + str(sys.argv[1]) + "/logs.txt"
	print("logging in: " + logFilePath)

	logger = logging.getLogger('Hyperlogger')
	logger.setLevel(logging.DEBUG)

	f_handler = logging.FileHandler(logFilePath)
	f_handler.setLevel(logging.DEBUG)

	f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	f_handler.setFormatter(f_format)
	logger.addHandler(f_handler)

	logger.info("--------------------------------------args: " + str(sys.argv[1]))

	s = time.perf_counter()
	asyncio.run(main())
	elapsed = time.perf_counter() - s
	print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# testing testing
