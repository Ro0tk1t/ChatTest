#! /usr/bin/python3
f = open('pw.txt','r')
while True:
    pw = f.readline()
    if pw == '':
        break
    else:
        print(pw.strip())


try:
    print('testTry')
    k = open('dggregre')
except:
    print('catched')
