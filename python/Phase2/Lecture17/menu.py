#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time
import sys


class Things():

    def do_something1(self):
        print("do something1 ... ...")
        time.sleep(1)
        print("something1 done!")

    def do_something2(self):
        print("do something2 ... ...")
        time.sleep(1)
        print("something2 done!")

    def do_something3(self):
        print("do something3 ... ...")
        time.sleep(1)
        print("something3 done!")


class Menu():
    def __init__(self):
        self.thing = Things()
        self.choices = {
            "1": self.thing.do_something1,
            "2": self.thing.do_something2,
            "3": self.thing.do_something3,
            "4": self.quit
        }

    def display_menu(self):
        print("""
Operation Menu:
1. Get List
2. Remove
3. Send Mail
4. Quit
""")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = input("Enter an option: ")
            except Exception as e:
                print("Please input a valid option!");continue

            choice = str(choice).strip()
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def quit(self):
        print("\nBye!\n")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()