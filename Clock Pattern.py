import os
from datetime import datetime
from time import sleep

symbol = '@'

inx = 0

#current_time = now.strftime("%S")
#print("Current Time is :", current_time)


def clear():
    os.system('cls')


# clear()
def call():
    global inx
    now = datetime.now()
    current_time = now.strftime("   %H:%M:%S")
    while inx < 7:
        for char in current_time:
            match char:
                case ' ':
                    space(inx)
                case ':':
                    sep(inx)
                case '0':
                    d0(inx)
                case '1':
                    d1(inx)
                case '2':
                    d2(inx)
                case '3':
                    d3(inx)
                case '4':
                    d4(inx)
                case '5':
                    d5(inx)
                case '6':
                    d6(inx)
                case '7':
                    d7(inx)
                case '8':
                    d8(inx)
                case '9':
                    d9(inx)
        inx += 1
        print()


def space(row):
    for col in range(2):
        print(' ', end=' ')




def sep(row):
    for col in range(2):
        if col == 0 and row in(1,4) :
            print(symbol, end=' ')

        else:
            print(' ', end=' ')



def d0(row):
    for col in range(6):
        if col in (0, 4) and row not in (0, 6):
            print(symbol, end=' ')
        elif col not in (0, 4, 5) and row in (0, 6):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def d1(row):
    for col in range(4):
        if col in (0, 2) and row == 6:
            print(symbol, end=' ')
        elif col == 1:
            print(symbol, end=' ')
        elif col == 0 and row == 1:
            print(symbol, end=' ')

        else:
            print(' ', end=' ')


def d2(row):
    for col in range(6):
        if col != 5 and row == 6:
            print(symbol, end=' ')
        elif row + col == 6 and col < 4:
            print(symbol, end=' ')
        elif col in (1, 2, 3) and row == 0:
            print(symbol, end=' ')
        elif col in (0, 4) and row in (1, 2):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def d3(row):
    for col in range(6):
        if col in (1, 2, 3) and row in (0, 3, 6):
            print(symbol, end=' ')
        elif col == 0 and row in (1, 5):
            print(symbol, end=' ')
        elif col == 4 and row in (1, 2, 4, 5):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def d4(row):
    for col in range(6):
        if col + row == 2:
            print(symbol, end=' ')
        elif row == 3 and col != 5:
            print(symbol, end=' ')
        elif col == 3:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def d5(row):
    for col in range(6):
        if col in (1, 2, 3) and row in (0, 2, 6):
            print(symbol, end=' ')
        elif col == 4 and row in (0, 3, 4, 5):
            print(symbol, end=' ')
        elif col == 0 and row in (0, 1, 2, 5):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def d6(row):
    for col in range(6):
        if col in (1, 2, 3) and row in (0, 2, 6):
            print(symbol, end=' ')
        elif col == 4 and row in ( 3, 4, 5):
            print(symbol, end=' ')
        elif col == 0 and row in ( 1, 2,3,4, 5):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')

def d7(row):
    for col in range(6):
        if col != 5 and row == 0:
            print(symbol, end=' ')
        elif row + col == 5 and col < 5 and col !=0:
            print(symbol, end=' ')
        elif col in (1, 2, 3) and row == 0:
            print(symbol, end=' ')
        elif col== 1 and row in (5, 6):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')

def d8(row):
    for col in range(6):
        if col in (1, 2, 3) and row in (0, 3, 6):
            print(symbol, end=' ')
        elif col in(0,4) and row in (1, 2, 4, 5):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')

def d9(row):
    for col in range(6):
        if col in (1, 2, 3) and row in (0, 4, 6):
            print(symbol, end=' ')
        elif col == 4 and row in (1, 2, 3, 4, 5):
            print(symbol, end=' ')
        elif col == 0 and row in ( 1, 2,3):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')

# call()
while 1 == 1:
    call()
    sleep(.9)
    inx=0
    clear()
