import MOTOR
import PUMP
import PWM_double
import datetime

def main(a,b,c,d):
    begin = datetime.datetime.now()             #加入计时模块
   
    PWM_double.PWM(a,b)
    PUMP.PUMP(c)
    MOTOR.MOTOR(d)
    end = datetime.datetime.now()               #加入计时模块
    print('总耗时：',end-begin)                            #打印程序运行时间

while True :
    a,b,c,d=map(int,input("angel,angel,pump,soil:").split(','))
    main(a,b,c,d)


 
