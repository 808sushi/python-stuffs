from math import *

print("a^2x + bx + c = 0")

check = False
while True:
    a = input("a = ")
    if a == "end":
        break
    b = input("b = ")
    c = input("c = ")
    x1 = 0
    x2 = 0

    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0:
        print("a must be != 0")
    else:
        check = True

    if check is True:
        delta = b * b - 4 * a * c

        if delta > 0:
            x1 = x1 + (-b + sqrt(delta)) / 2 * a
            x2 = x2 + (-b - sqrt(delta)) / 2 * a
            print("the roots of the equation are: x1 = " + str(x1) + ", x2 = " + str(x2))
        if delta == 0:
            x1 = -b / (2 * a)
            print("the root of the equation is: x1 = x2 = " + str(x1))
        if delta < 0:
            print("exists no x value")
