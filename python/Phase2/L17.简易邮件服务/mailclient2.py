#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

from pick import pick


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

	option, pos = pick(menulist, "Enter an option: ")
	if pos == 0:
		#Get List
		run('list;%s' % myname)
		input('press any key to continue...')
	elif pos == 1:
		# Remove
		mailid = input('input mailid:')
		run('remove;%s;%s' % (myname, mailid))
		input('press any key to continue...')
	elif pos == 2:
		# Send Mail
		to = input('input reciver:\n')
		msg = input('input message:\n')
		run('send;%s;%s;%s'% (myname, to, msg))
		input('press any key to continue...')
	else:
		print('\nBye!\n')
		break
	print('\n\n')	



