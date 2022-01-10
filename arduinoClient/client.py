#!/usr/bin/python
# -*- coding: utf-8 -*-
import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)

encoding = 'utf-8'


def write(arduinoToWrite, data):

    arduinoToWrite.write(bytes(data, encoding))
    time.sleep(.05)


def read(arduinoToRead):

    return arduinoToRead.readline()


while True:

    write(arduino, input('send to Arduino: '))
