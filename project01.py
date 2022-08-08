#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project#001 V1.0
#
# github.com/hnralmeida/osorim/project01
#

import RPi.GPIO
import serial
from time import sleep
import sys

g.setmode(g.BOARD)

# Iniciando Sensor UltraSonico
trig1 = 11
echo1 = 13
echo2 = 15
trig2 = 16

g.setup(trig1, g.OUT)
g.setup(trig2, g.OUT)
g.setup(echo1, g.IN)
g.setup(echo2, g.IN)

# Iniciando Motores
ena = 12
enb = 32
in1 = 29
in2 = 31
in3 = 35
in4 = 37

g.setup(in1, g.OUT)
g.setup(in2, g.OUT)
g.setup(in3, g.OUT)
g.setup(in4, g.OUT)

g.setup(ena, g.OUT)
g.setup(enb, g.OUT)

g.output(in1, g.HIGH)
g.output(in2, g.LOW)
g.output(in3, g.HIGH)
g.output(in4, g.LOW)

m1 = g.PWM(ena, 1000)
m2 = g.PWM(enb, 1000)

m1.start(25)
m2.start(25)

time.sleep(1)

def motor1(x):
    if x=='r':
        if(temp1==1):
            g.output(in1,g.HIGH)
            g.output(in2,g.LOW)
            print("Motor 2 turned forward")
        else:
            g.output(in1,g.LOW)
            g.output(in2,g.HIGH)
            print("Motor 2 turned backward")

    elif x=='s':
        print("Motor 2 has stopped")
        g.output(in1,g.LOW)
        g.output(in2,g.LOW)

    elif x=='f':
        print("Motor 2 turned forward")
        g.output(in1,g.HIGH)
        g.output(in2,g.LOW)
        temp1=1

    elif x=='b':
        print("Motor 2 turned backward")
        g.output(in1,g.LOW)
        g.output(in2,g.HIGH)
        temp1=0

    elif x=='l':
        print("Motor 1 is in low speed now")
        m1.ChangeDutyCycle(25)

    elif x=='m':
        print("Motor 1 is in medium speed now")
        m1.ChangeDutyCycle(50)

    elif x=='h':
        print("Motor 1 is in high speed now")
        m1.ChangeDutyCycle(100)
    
    elif x=='e':
        g.cleanup()
        print("GPIO Clean up")
        exit()
    
    else:
        print("<<<  wrong entry  >>>")
        print("please enter ta valid command to continue.....")
        
def motor2(x):
    if x=='r':
        if(temp2==1):
            g.output(in3,g.HIGH)
            g.output(in4,g.LOW)
            print("Motor 2 turned forward")
        else:
            g.output(in3,g.LOW)
            g.output(in4,g.HIGH)
            print("Motor 2 turned backward")

    elif x=='s':
        print("Motor 2 has stopped")
        g.output(in3,g.LOW)
        g.output(in4,g.LOW)

    elif x=='f':
        print("Motor 2 turned forward")
        g.output(in1,g.HIGH)
        g.output(in2,g.LOW)
        temp2=1

    elif x=='b':
        print("Motor 2 turned backward")
        g.output(in3,g.LOW)
        g.output(in4,g.HIGH)
        temp2=0

    elif x=='l':
        print("Motor 2 is in low speed now")
        m2.ChangeDutyCycle(25)

    elif x=='m':
        print("Motor 2 is in medium speed now")
        m2.ChangeDutyCycle(50)

    elif x=='h':
        print("Motor 2 is in high speed now")
        m2.ChangeDutyCycle(100)
    
    elif x=='e':
        g.cleanup()
        print("GPIO Clean up")
        exit()
    
    else:
        print("<<<  wrong entry  >>>")
        print("please enter ta valid command to continue.....")

def distControl():
    try:
        init_t = 0
        end_t = 0
        
        g.output(trig1,g.LOW)
        time.sleep(0.2)
        g.output(trig1, g.HIGH)
        time.sleep(0.2)
        g.output(trig1,g.LOW)

        while g.input(echo1) == 0 :
            init_t = time.time()

        while g.input(echo1) == 1 :
            end_t = time.time()

        tempo = end_t - init_t
        dist1 = (tempo * 17150)    ## velocidade = 34300 cm/s
                                    ## ida e volta
        g.output(trig2,g.LOW)
        time.sleep(0.2)
        g.output(trig2, g.HIGH)
        time.sleep(0.2)
        g.output(trig2,g.LOW)

        while g.input(echo2) == 0 :
            init_t2 = time.time()

        while g.input(echo2) == 1 :
            end_t2 = time.time()

        tempo = end_t - init_t
        dist2 = (tempo * 17150)    ## velocidade = 34300 cm/s
                                    ## ida e volta
        print(f"Dist1: {dist1} \t Dist2: {dist2}")
        return [dist1, dist2]
                                   
    except KeyboardInterrupt:
        g.cleanup()

def main():
    # for serial reading is used
    #     line = ser.readline().decode('utf-8').rstrip()
    ser = serial.Serial('dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    
    
    
    ser.close()
    
if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt):
        pass
    
    
