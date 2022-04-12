import RPi.GPIO as g
import sys
import time
import threading

g.setmode(g.BOARD)
trig1 = 11
echo1 = 13
echo2 = 15
trig2 = 16
ena = 12
enb = 32
in1 = 29
in2 = 31
in3 = 35
in4 = 37

# Iniciando Sensor UltraSonico
g.setup(trig1, g.OUT)
g.setup(trig2, g.OUT)
g.setup(echo1, g.IN)
g.setup(echo2, g.IN)

# Iniciando Motores
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

def motorControl(char x):
    #print("\n")
    #print("The default speed & direction of motor is LOW & Forward.....")
    #print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
    #print("\n")
    
    while(1):
        #x=input()
        if x=='r':
            print("run")
            if(temp1==1):
             g.output(in1,g.HIGH)
             g.output(in2,g.LOW)
             g.output(in3,g.HIGH)
             g.output(in4,g.LOW)
             print("forward")
            else:
             g.output(in1,g.LOW)
             g.output(in2,g.HIGH)
             g.output(in3,g.LOW)
             g.output(in4,g.HIGH)
             print("backward")

        elif x=='s':
            print("stop")
            g.output(in1,g.LOW)
            g.output(in2,g.LOW)
            g.output(in3,g.LOW)
            g.output(in4,g.LOW)

        elif x=='f':
            print("forward")
            g.output(in1,g.HIGH)
            g.output(in2,g.LOW)
            g.output(in3,g.HIGH)
            g.output(in4,g.LOW)
            temp1=1

        elif x=='b':
            print("backward")
            g.output(in1,g.LOW)
            g.output(in2,g.HIGH)
            g.output(in3,g.LOW)
            g.output(in4,g.HIGH)
            temp1=0

        elif x=='l':
            print("low")
            m1.ChangeDutyCycle(25)
            m2.ChangeDutyCycle(25)

        elif x=='m':
            print("medium")
            m1.ChangeDutyCycle(50)
            m2.ChangeDutyCycle(50)

        elif x=='h':
            print("high")
            m1.ChangeDutyCycle(100)
            m2.ChangeDutyCycle(100)
        
        elif x=='e':
            g.cleanup()
            print("GPIO Clean up")
            break
        
        else:
            print("<<<  wrong entry  >>>")
            print("please enter ta valid command to continue.....")

def sensorControl():
    try:
        init_t1 = 0
        end_t1 = 0
        init_t2 = 0
        end_t2 = 0
        
        while(True) :
            g.output(trig1,g.LOW)
            time.sleep(0.2)
            g.output(trig1, g.HIGH)
            time.sleep(0.2)
            g.output(trig1,g.LOW)
            
            while g.input(echo1) == 0 :
                init_t1 = time.time()
                
            while g.input(echo1) == 1 :
                end_t1 = time.time()
                
            g.output(trig2,g.LOW)
            time.sleep(0.2)
            g.output(trig2, g.HIGH)
            time.sleep(0.2)
            g.output(trig2,g.LOW)
            
            while g.input(echo2) == 0 :
                init_t2 = time.time()
                
            while g.input(echo2) == 1 :
                end_t2 = time.time()
                
            tempo1 = end_t1 - init_t1
            tempo2 = end_t2 - init_t2
            dist1 = (tempo1 * 17000) ## velocidade = 34000 cm/s
            dist2 = (tempo2 * 17000) ## ida e volta
            print(f"Dist1: {dist1} \t Dist2: {dist2}")
                                   
    except KeyboardInterrupt:
        g.cleanup()

if __name__ == "__main__":
    motorControl()


