name = input("Enter your name (include A-Z):")
symbol = input("Enter your favorite symbol:")
print()
inx = 0
name = name.upper()
name = name.strip()
name = ' '+name


def call():
    global inx
    while inx < 7:
        for char in name:
            match char:
                case ' ':
                    space(inx)
                case 'A':
                    a(inx)
                case 'B':
                    b(inx)
                case 'C':
                    c(inx)
                case 'D':
                    d(inx)
                case 'E':
                    e(inx)
                case 'F':
                    f(inx)
                case 'G':
                    g(inx)
                case 'H':
                    h(inx)
                case 'I':
                    i(inx)
                case 'J':
                    j(inx)
                case 'K':
                    k(inx)
                case 'L':
                    l(inx)
                case 'M':
                    m(inx)
                case 'N':
                    n(inx)
                case 'O':
                    o(inx)
                case 'P':
                    p(inx)
                case 'Q':
                    q(inx)
                case 'R':
                    r(inx)
                case 'S':
                    s(inx)
                case 'T':
                    t(inx)
                case 'U':
                    u(inx)
                case 'V':
                    v(inx)
                case 'W':
                    w(inx)
                case 'X':
                    x(inx)
                case 'Y':
                    y(inx)
                case 'Z':
                    z(inx)

        inx += 1
        print()


def space(row):
    for col in range(3):
        print(' ', end=' ')


def a(row):
    for col in range(6):
        if col == 4 and row in {1, 2}:
            print(symbol, end=' ')
        elif (row in (0, 3)) and (col in (1, 2, 3)):
            print(symbol, end=' ')
        elif col in (0, 4) and row != 0:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def b(row):
    for col in range(6):
        if col == 0:
            print(symbol, end=' ')
        elif (row in (0, 3, 6)) and (col in (1, 2, 3)):
            print(symbol, end=' ')
        elif (row in (1, 2, 4, 5)) and (col == 4):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def c(row):
    for col in range(6):
        if col == 0 and row not in (0, 6):
            print(symbol, end=' ')
        elif col not in (0, 4, 5) and row in (0, 6):
            print(symbol, end=' ')
        elif row in (1, 5) and (col == 4):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def d(row):
    for col in range(6):
        if col == 0:
            print(symbol, end=' ')
        elif col == 4 and row in (2, 3, 4):
            print(symbol, end=' ')
        elif row in (0, 6) and col in (1, 2):
            print(symbol, end=' ')
        elif row in (1, 5) and col == 3:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def e(row):
    for col in range(6):
        if col == 0:
            print(symbol, end=' ')
        elif row in (0, 3, 6) and col != 5:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def f(row):
    for col in range(6):
        if col == 0:
            print(symbol, end=' ')
        elif row in (0, 3) and col != 5:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def g(row):
    for col in range(6):
        if col == 0 and row not in (0, 6):
            print(symbol, end=' ')
        elif col not in (0, 4, 5) and row in (0, 6):
            print(symbol, end=' ')
        elif row in (1, 4, 5,) and (col == 4):
            print(symbol, end=' ')
        elif row in (3, 4,) and (col == 2):
            print(symbol, end=' ')
        elif row == 3 and (col == 3):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def h(row):
    for col in range(6):
        if col in (0, 4):
            print(symbol, end=' ')
        elif row == 3 and col != 5:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def i(row):
    for col in range(4):
        if col == 1:
            print(symbol, end=' ')
        elif row in (0, 6) and col in (0, 2):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def j(row):
    for col in range(4):
        if col == 2:
            print(symbol, end=' ')
        elif row in (0, 6) and col == 1:
            print(symbol, end=' ')
        elif row == 5 and col == 0:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def k(row):
    for col in range(6):
        if col == 0:
            print(symbol, end=' ')
        elif row + col == 4 or row - col == 2:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def l(row):
    for col in range(6):
        if col == 0:
            print(symbol, end=' ')
        elif row == 6 and col not in (5, 6):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def m(row):
    for col in range(6):
        if col in (0, 4):
            print(symbol, end=' ')
        elif row == 2 and col in (1, 3):
            print(symbol, end=' ')
        elif row in (3, 4) and col == 2:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def n(row):
    for col in range(6):
        if col in (0, 4):
            print(symbol, end=' ')
        elif row - col == 1 and col != 5:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def o(row):
    for col in range(6):
        if col in (0, 4) and row not in (0, 6):
            print(symbol, end=' ')
        elif col not in (0, 4, 5) and row in (0, 6):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def p(row):
    for col in range(6):
        if col == 4 and row in {1, 2}:
            print(symbol, end=' ')
        elif (row in (0, 3)) and (col in (1, 2, 3)):
            print(symbol, end=' ')
        elif col == 0:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def q(row):
    for col in range(6):
        if col in (0, 4) and row not in (0, 5, 6):
            print(symbol, end=' ')
        elif col not in (0, 4, 5) and row in (0, 5):
            print(symbol, end=' ')
        elif col == 4 and row == 6:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def r(row):
    for col in range(6):
        if col == 4 and row in {1, 2}:
            print(symbol, end=' ')
        elif (row in (0, 3)) and (col in (1, 2, 3)):
            print(symbol, end=' ')
        elif col == 0:
            print(symbol, end=' ')
        elif row - col == 2:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def s(row):
    for col in range(6):
        if col == 0 and row in (1, 2, 5):
            print(symbol, end=' ')
        elif col in (1, 2,3) and row in (0, 3, 6):
            print(symbol, end=' ')
        elif col == 4 and row in (1, 4, 5):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def t(row):
    for col in range(6):
        if col == 2 or row == 0 and col != 5:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def u(row):
    for col in range(6):
        if col in (0, 4) and row != 6:
            print(symbol, end=' ')
        elif col not in (0, 4, 5) and row == 6:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def v(row):
    for col in range(6):
        if col in (0, 4) and row not in (5, 6):
            print(symbol, end=' ')
        elif col in (1, 3) and row == 5:
            print(symbol, end=' ')
        elif col == 2 and row == 6:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def w(row):
    for col in range(6):
        if col in (0, 4):
            print(symbol, end=' ')
        elif col == 2 and row in (1, 2, 3, 4):
            print(symbol, end=' ')
        elif row == 5 and col in (1, 3):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def x(row):
    for col in range(6):
        if (col < 3 and col == row) or (row < 2 and row + col == 4):  # or (row > 4 and row - col == 2):
            print(symbol, end=' ')
        elif (row > 3 and col + row == 6) or (row > 4 and row - col == 2):  # or (row > 4 and row - col == 2):
            print(symbol, end=' ')
        elif col == 2 and row == 3:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def y(row):
    for col in range(6):
        if col == 2 and row > 2:
            print(symbol, end=' ')
        elif row in (0, 1) and col in (0, 4):
            print(symbol, end=' ')
        elif row == 2 and col in (1, 3):
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


def z(row):
    for col in range(6):
        if row in (0, 6) and col != 5:
            print(symbol, end=' ')
        elif col + row == 5 and row != 0:
            print(symbol, end=' ')
        else:
            print(' ', end=' ')


call()
