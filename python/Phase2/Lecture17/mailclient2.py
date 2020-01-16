#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

# pip3 install tty_menu
from tty_menu import tty_menu


def run(cmd):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.sendto(cmd.encode('utf-8'), ('127.0.0.1', 9999))
	print(s.recv(1024).decode('utf-8'))
	s.close()

myname = 'noname'
if len(sys.argv) == 1:
	myname = input('input your name:')
elif len(sys.argv) == 2:
	myname = sys.argv[1] # get name from command args


menulist = ['Get List','Remove','Send Mail','Quit']
while True:

	pos = tty_menu(menulist, ("Hello %s, enter an option: " % myname))
	if pos == 0:
		#Get List
		run('list;%s' % myname)

	elif pos == 1:
		# Remove
		mailid = input('input mailid:')
		run('remove;%s;%s' % (myname, mailid))

	elif pos == 2:
		# Send Mail
		to = input('input reciver:\n')
		msg = input('input message:\n')
		run('send;%s;%s;%s'% (myname, to, msg))

	else:
		print('\nBye!\n')
		break
	print('\n\n')	



