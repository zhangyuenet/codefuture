# pip3 install tty_menu

from tty_menu import tty_menu

menulist = ['Get List','Remove','Send Mail','Quit']
pos = tty_menu(menulist, "Enter an option: ")
print("your choice is %s" % menulist[pos])
