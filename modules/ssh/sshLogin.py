#! /usr/bin/python3
from pexpect import pxssh
import sys, threading

class moduleStruct:
    def __init__(self,user,passwd,host,port=22):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port =port

    def doc():
        #return all about the module
        return

    def info(cursor):
        sql = 'select * from info;'
        try:
            cursor.execute(sql)
            infos = cursor.fetchone()
        except:
            print('[-] not fund info for module %s'%(moduleName))
        info = infos[0]
        print(info)     ##需格式化输出
        return info

    def connect(user,pw,host):
        conn = pxssh.pxssh()
        conn.login(host,user,pw)
        return conn
    
    def cmdExec(conn,cmd):
        conn.sendline(cmd)
        conn.prompt()
        print(conn.before.decode('ascii'))
        return conn
    
    def main(self):
        user = self.user
        pw = self.passwd
        host = self.host
        ssh = connect(user,pw,host)
        while True:
            print('%s@%s $> '%(user,host),end='')
            cmd = input()
            cmdExec(ssh,cmd)
            if cmd == 'logout':
                sys.exit()

