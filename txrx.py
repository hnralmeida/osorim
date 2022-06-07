#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Raspberry Pi to Arduino Serial Communication

import serial

if __name__ == '__main__':
  ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
  ser.flush()
  file1 = open("data.txt","a")
  
  while True:
    if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip()
      print(line)
      file1 = open("data.txt","a")
      line2 = str(line) + " \n"
      file1.write(line2)
      file1.close()
