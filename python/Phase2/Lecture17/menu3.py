# pip3 install tty_menu

from tty_menu import tty_menu

menulist = ['Get List','Remove','Send Mail','Quit']

while True:
	pos = tty_menu(menulist, "Enter an option: ")
	if pos == 0:
		#Get List
		print('Get List')

	elif pos == 1:
		# Remove
		print('Remove')

	elif pos == 2:
		# Send Mail
		print('send mail')

	else:
		print('\nBye!\n')
		break



