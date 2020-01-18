#pip install pick
#pip install windows-curses (only on windows)


from pick import pick

menulist = ['Get List','Remove','Send Mail','Quit']

while True:
	option, pos = pick(menulist, "Enter an option: ")
	if pos == 0:
		#Get List
		print('Get List')
		input('press any key to continue...')

	elif pos == 1:
		# Remove
		print('Remove')
		input('press any key to continue...')

	elif pos == 2:
		# Send Mail
		print('send mail')
		input('press any key to continue...')

	else:
		print('\nBye!\n')
		break



