#! /usr/bin/python3.6
import sys
import os
import re
import pymysql
import configparser

print('''
PentestToolSet
Write By Rootkit
version -> 1.0
''')

def doc():
    #print(globals()['__doc__'])
    '''
    use             -> use moduls
    show            -> print options
    info            -> info of modules
    exploit         -> start exploit
    
    -h  --help  show help
    '''

def readConf():
    cf = configparser.ConfigParser()
    #cf.read('/etc/pts.conf')
    cf.read('pts.conf')
    sections = cf.sections()
    return cf
    #modulesPath = os.getcwd()+'/modules/'

#连接数据库
def connMysql(user,passwd,port,database):
    try:
        conn = pymysql.connect(user=user,host='localhost',port=int(port),db=database)
        cur = conn.cursor()
        return cur
    except:
        print('[-] connect database error')
    #return cur

#选择模块方法
def use(moduleType,moduleName):
    global module
    global status
    #如果存在此模块则加载之
    if os.path.exists(modulesPath+moduleType+moduleName+'.py'):
        os.chdir(modulesPath+moduleType)
        print(os.system('ls'))
        m = __import__(str(moduleName))
        #实例化一个模块
        module = m.moduleStruct
        status = 1
    else:
        status = 0
    return module

#控制相关信息
def show(Type):
    print('more info of %s: '%Type)
    if Type == 'options':
        pass
    else:
        os.system('ls -lh %s/%s'%(modulePath,Type))
    return Type

#模块相关信息
def info(module):
    print('info of module %s: '%module)
    return 

#模块的参数设置
def set(selection):
    global module
    global status
    if hasattr(module,selection):
        setattr(module,selection,)
        status = 1
    else:
        status = 0
    return status

#利用
def exploit():
    return 

#模块检索
def search(module):
    desc = os.system('find modules/* -name %s'%module)
    return desc

def main():
    global moduleName
    while True:
        print("pts(\033[1;3;30;41;7m%s\033[0m)> "%moduleName,end='')
        op = input()
        if op == 'exit':
            exit(0)
        try:
            #select = ops.index(op)
            #分割用户的输入
            opt = re.findall(r'\S+',op)
            #按第一个选项判断应使用哪个方法
            if opt[0] == 'use':
            #后面可能有多个参数，只取第二个操作符
                #moduleName = re.findall(r'/(\S+)$',opt[1])[0]
                moduleType = (opt[1].split(moduleName))[0]
                module = use(moduleType,moduleName)
                if status == 0:
                    print('[-] %s not exist'%module)
                else:
                    moduleName = module.name

            elif opt[0] == 'show':
                show(opt[1])

            elif opt[0] == 'info':
                #assert cursors = connMysql
                sql = 'select * from modules where name="%s";'%moduleName
                cursors.execute(sql)
                allInfo = cursors.fatchall()
                ####在这里格式化输出模块信息

            elif opt[0] == 'set':
                #判断是否加载模块，然后设置参数
                if module == None:
                    print('[-] no module selected')
                    break
                else:
                    set(opt[1],opt[2])
                    if status == 1:
                        print('[+] %s => %s'%(opt[1],opt[2]))
                    else:
                        print('[-] there has no attribute %s'%opt[1])
                        break

            else:
                #如找不到方法，则视为系统命令并执行
                #if len(opt) != 0:
                    os.system(op)
        except:
            print('[-] unknown option "%s"'%op)
            print(doc.__doc__)

if __name__ == '__main__':
    #ops = ['use','show']
    cf = readConf()
    modulesPath = cf.get('module','modulesPath')
    databaseType = cf.get('db','databaseType')
    user = cf.get('db','username')
    passwd = cf.get('db','passwd')
    port = cf.get('db','port')
    database = cf.get('db','database')
    moduleName = None
    module = None                   #全局模块变量
    status = 0                      #全局状态变量
    if (not os.path.exists(modulesPath)) & (not os.path.isfile(modulesPath)):
        print('[-] Can\'t find module path! please check configure')
    with connMysql(user,passwd,port,database) as cursors:      #上下文数据库连接
        main()
