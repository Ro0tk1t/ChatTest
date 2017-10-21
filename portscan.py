from socket import *
from argparse import ArgumentParser
from time import *
import threading

threads = []
def singlePort(ip,port):      #套接字判断端口开启情况
    if port:
        try:
            connTcp = socket(AF_INET,SOCK_STREAM)
            connTcp.connect((ip,port))
            print('Scan for %s : \n'%ip)
            print('     port %s is open !\n'%port)
            connTcp.close()
        except:
            print('port %s is close'%port)

def portScan(ip,port):
    x = port.split('-')
    if len(x) == 2:
        portStart = int(x[0])
        portEnd = int(x[1])
        #装载线程
        for i in range(portStart,portEnd):
            t = threading.Thread(target=singlePort,args=(ip,i))
            t.setDaemon(True)
            threads.append(t)
        #启动线程
        for t in threads:
            t.start()
        #阻塞前台线程
        for t in threads:
            t.join()
    elif len(x) == 1:
        singlePort(ip,int(x[0]))

    else:
        print('wrong port format')
        exit(0)
