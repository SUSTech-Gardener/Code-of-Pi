# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
from time import sleep
import numpy as np
num=np.array([135,0])
#将舵机度数转换为信号占空比，0-180度线性对应2.5%-12.5%的占空比


import RPi.GPIO as GPIO
import time
import numpy as np
num=np.array([135,45])                #定义num为全局变量

def tonum(a,b):
   
    #fm0=10/270
    #fm1=10/180
    a=(a*0.037+2.5)*10
    b=(b*0.055+2.5)*10
    #print(a,b)
 
    global num            #声明可以修改全局变量
    num =np.array([a/10,b/10])
    #print(num)
#     return num

#a,b=map(int,input("Please input both angle of the platform:").split(","))
#num[0],num[1]=map(int,input("Please input both angle of the platform:").split(","))
#print(tonum(a,b))
#print(num[0])


GPIO.setwarnings(False)             #忽略警告
GPIO.setmode(GPIO.BCM) #设置gpio引脚编号模式，有两种编号模式可供选择，自己随意设置就好
GPIO.setup(13, GPIO.OUT) #设置13号口为输出模式
p13 = GPIO.PWM(13, 50) #设置13号口为PWM信号，标定频率为50HZ
p13.start(0) #初始化舵机度数为0

GPIO.setmode(GPIO.BCM) #设置gpio引脚编号模式，有两种编号模式可供选择，自己随意设置就好
GPIO.setup(12, GPIO.OUT) #设置12号口为输出模式
p12 = GPIO.PWM(12, 50) #设置12号口为PWM信号，标定频率为50HZ
p12.start(0) #初始化舵机度数为0


def PWM(a,b):
#     a,b=map(int,input("Please input both angle of the platform:").split(','))
                                    #请求用户输入转到多少度
    tonum(a,b)
    if min(a,b)<=0 or a>270 or b>180 :
        p13.stop() #停止端口占用（很重要）
        p12.stop() 
        exit() #如果输入不正确则退出
    else:
        print(a,b)
        p13.ChangeDutyCycle(num[0]) #否则改变P13口的占空比为对应占空比
        p12.ChangeDutyCycle(num[1])
        sleep(0.1)
        p13.ChangeDutyCycle(0) #clean the dutycycle to prevent the motor move unregular
        p12.ChangeDutyCycle(0)
        
        