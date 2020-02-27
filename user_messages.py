import os
import time


class UserInterface:
    @staticmethod
    def clear():
        time.sleep(1)
        os.system('cls')

    @staticmethod
    def choice():
        return input("""Hello! Choose: 
A - Vehicle registration
B - Driving license
C - ID

Type here: """).upper()

    @staticmethod
    def secret_choice():
        return input("""Dear official,
choose who is gonna be the next user: """).upper()

    @staticmethod
    def new_user(letter, number):
        print(f'Your number is {letter}{number}')

    @staticmethod
    def next_user(letter, number):
        if number is None:
            print("No more people in this queue")
        else:
            print(f'Next user is {letter}{number}')
