import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.OUT)

def PUMP(a):
    if a==1:
        GPIO.output(6,GPIO.HIGH)
        print("喷水中")
#         time.sle0ep(4)
#         GPIO.output(6,GPIO.LOW)
        print('end')
    elif a==0:
        GPIO.output(6,GPIO.LOW)
        print('end')
#         time.sleep(1)
    else:
        print('Error')


if __name__=="__main__":
    b=input("Please input your order,1 is start 0 is stop:")
    b=int(b)
    PUMP(b)