from math import *

n = int(input("n: "))
a = int(input("a: "))
b = int(input("b: "))

S = 0

for i in range(1, n + 1):
    S = S + (a * i + b * floor(sqrt(n)))


s = S % (pow(10, 9) + 7)
print(s)