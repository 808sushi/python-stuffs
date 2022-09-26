import random

print("this is a code generator")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j" , "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

word = input("whatever word you wanna encode: ")

w = list(word)

def print_encoded():
    for letters in w:
        print(letters, end="")
    print("\n")

for i in range(len(word)):
    w[i] = random.choice((alphabet))

print_encoded()