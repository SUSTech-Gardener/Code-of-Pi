#!usr/bin/python

import MOTOR
import PUMP
import PWM_double
import datetime
import socket
import threading


# 处理客户端的请求操作
def handle_client_request(service_client_socket, ip_port):
    while True:
        recv_data = service_client_socket.recv(1024)
        if recv_data.decode('utf8')=="NoTarget":
            control(135,45,0,0)
            print(recv_data.decode('utf8'))
        else:
            print(recv_data.decode('utf8'), ip_port)
            x,y=map(float,recv_data.decode('utf8').split(','))
            if 0<x<=384:
                a=90
                control(a,40,1,0)
#                return [150,45,1,0]             #1920 1080
            elif 384<x<=768:
                a=112.5
                control(a,40,1,0)
            elif 768<x<=1152:
                a=135
                control(a,40,1,0)
            elif 1152<x<=1536:
                a=112.5
                control(a,40,1,0)
            elif 1536<x<=1920:
                a=180
                control(a,40,1,0)
            else:
                control(135,45,0,0)
    

                
            #service_client_socket.send('ok, 问题正在处理中...'.encode('utf8'))
#             print('客户端下线了:', ip_port)
            #print('no weed !')
            #return [135,45,1,0]



def control(a,b,c,d):
    begin = datetime.datetime.now()             #加入计时模块
    PWM_double.PWM(a,b)
    PUMP.PUMP(c)
    MOTOR.MOTOR(d)
    end = datetime.datetime.now()               #加入计时模块
    print('总耗时：',end-begin)                            #打印程序运行时间


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 9000))
    # 最大等待连接数为128
    tcp_server_socket.listen(128)
    #i=1
    while True :
        service_client_socket, ip_port = tcp_server_socket.accept()
        print('客户端连接成功', ip_port)
        handle_client_request(service_client_socket,ip_port)

        #control(a,b,c,d)
        #print(i+1)


 
