import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)             #Represent M1
GPIO.setup(17,GPIO.OUT)            #Represent M2
GPIO.setup(27,GPIO.OUT)            #Represent M3
GPIO.setup(22,GPIO.OUT)            #Represent M4
alllist=[4,17,27,22]


def MOTOR(a):
    GPIO.setup(alllist,GPIO.LOW)
    if a==2:                                #1 is run forward   
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        print('Let`s Backward')
#         time.sleep(1)
    elif a==1:                              #2 is run backward
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        print('Let`s Forkward')
    elif a==0:
        GPIO.setup(4,GPIO.HIGH)             #Represent M1
        GPIO.setup(17,GPIO.HIGH)            #Represent M2
        GPIO.setup(27,GPIO.LOW)             #Represent M3
        GPIO.setup(22,GPIO.LOW)  
    else:
        print('Input Error')

if __name__=="__main__":
    c=input('1 is forward,2 is backward:')
    c=int(c)
    MOTOR(c)