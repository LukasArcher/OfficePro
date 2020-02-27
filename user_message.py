import os
import time


def clear():
    time.sleep(1)
    os.system('cls')


def choice():
    return input("""Hello! Choose: 
A - Vehicle registration
B - Driving license
C - ID

Type here: """).upper()


def secret_choice():
    return input("""Dear official,
choose who is gonna be the next user: """).upper()


def vip_choice():
    return input("""I see you are VERY IMPORTANT PERSON. Choose:
A - Vehicle registration
B - Driving license
C - ID

Type here: """).upper()


def new_user(letter, number):
    print(f'Your number is {letter}{number}')

def next_user(letter, number):
    if number is None:
        print("No more people in this queue")
    else:
        print(f'Next user is {letter}{number}')


def error():
    return "You are fucking dumb! Try again!"
