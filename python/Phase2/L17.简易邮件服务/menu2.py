#pip install pick
#pip install windows-curses (only on windows)


from pick import pick

options = ['Get List','Remove','Send Mail','Quit']
option, index = pick(options, 'Enter an option:')
print(option)
print(index)

