#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mail Server example
# CodeFuture@CA

import socket


maillist = {} # {id:value} value=[from,to,msg]
ticker = 1000


def getnextnumber():
    global ticker
    ticker += 1
    return str(ticker)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
print('UDP contact server started...')


#list;name
#remove;name;id
#Send;from;to;msg

while True:
    # 接受一个新连接:
     # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    arg = data.decode('utf-8').split(';')
    if len(arg) <= 1:
        s.sendto('ERROR: bad command'.encode('utf-8'), addr)
        continue #bad args
    if arg[0] == 'send':
        if len(arg) != 4:
            s.sendto('ERROR：bad args.'.encode('utf-8'), addr)
            continue

        maillist[getnextnumber()] = [arg[1],arg[2],arg[3]]
        s.sendto(('mail to %s, sent by %s' % (arg[2] , arg[1])).encode('utf-8'), addr)

    elif arg[0] == 'remove':
        if len(arg) != 3:
            s.sendto('ERROR：bad args.'.encode('utf-8'), addr)
            continue

        name = arg[1]
        mailid = arg[2]
        print("name=%s, mailid=%s" % (name, mailid))
        if mailid in maillist:
            #判断邮件的所有者是否正确 
            if maillist[mailid][1] == name:
                maillist.pop(mailid)
                s.sendto(('mail id %s is removed' % mailid).encode('utf-8'), addr)
            else:
                s.sendto('ERROR：No permission.'.encode('utf-8'), addr)
        else:
            s.sendto('Not found'.encode('utf-8'), addr)

    elif arg[0] == 'list':
        if len(arg) != 2:
            s.sendto('ERROR：bad args.'.encode('utf-8'), addr)
            continue

        name = arg[1]
        resultlist = []
        for mailid in maillist.keys():
            if maillist[mailid][1] == name:
                resultlist.append('-- %s -- %s : %s' % (mailid, maillist[mailid][0], maillist[mailid][2]))
        if len(resultlist) > 0:
            s.sendto( ('\r\n'.join(resultlist)).encode('utf-8') ,addr)
        else:
            s.sendto('Not found'.encode('utf-8'), addr)
    else:
        s.sendto('ERROR: bad command'.encode('utf-8'), addr)

    #print(maillist) #查看当前所有数据
