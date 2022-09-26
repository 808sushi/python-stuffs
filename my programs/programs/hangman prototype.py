import random

print("welcome to hangman")
print("guess each letter, you have 5 guesses")

words = ["pycharm", "coding", "pain"]

pycharm = ["_", "_", "_", "_", "_", "_", "_"]
coding = ["_", "_", "_", "_", "_", "_"]
pain = ["_", "_", "_", "_"]

def get_word():
    word = random.choice(words)
    return word.lower()

word = get_word()

def print_pycharm():
    for space in pycharm:
        print(space, end="")

    print("\n")

def print_coding():
    for space in coding:
        print(space, end="")

    print("\n")

def print_pain():
    for space in pain:
        print(space, end="")

    print("\n")

if word == "pycharm":
    print_pycharm()
    print("hint: its this program you're using")
elif word == "coding":
    print_coding()
    print("hint: the action of creating a program")
elif word == "pain":
    print_pain()
    print("hint: what i experience every day")

guessed_letters = []
guesses = 0

chances = 5
while True:

    user_input = input("enter a letter or type \"quit\" to quit: ").lower()

    if user_input == "quit":
        print("game ended. have a nice day")
        break

    def check_input():

        if user_input in guessed_letters:
            print("you already guessed that letter")

        if len(user_input) == 1 and user_input.isalpha():
            pass
        else:
            print("invalid input, please only enter one letter")
    check_input()

    if user_input not in word and user_input not in guessed_letters and user_input.isalpha() and len(user_input) == 1:
        chances -= 1

    # pycharm
    if word == "pycharm":
        if user_input == "p":
            pycharm[0] = "p"
            guesses += 1
            guessed_letters.append(user_input)
            print_pycharm()
        elif user_input == "y":
            pycharm[1] = "y"
            guesses += 1
            guessed_letters.append(user_input)
            print_pycharm()
        elif user_input == "c":
            pycharm[2] = "c"
            guesses += 1
            guessed_letters.append(user_input)
            print_pycharm()
        elif user_input == "h":
            pycharm[3] = "h"
            guesses += 1
            guessed_letters.append(user_input)
            print_pycharm()
        elif user_input == "a":
            pycharm[4] = "a"
            guesses += 1
            guessed_letters.append(user_input)
            print_pycharm()
        elif user_input == "r":
            pycharm[5] = "r"
            guesses += 1
            guessed_letters.append(user_input)
            print_pycharm()
        elif user_input == "m":
            pycharm[6] = "m"
            guesses += 1
            guessed_letters.append(user_input)
            print_pycharm()
        elif user_input not in word and user_input not in guessed_letters and user_input.isalpha() and len(user_input) == 1:
            print(user_input + " is not in the word")
            print("you have " + str(chances) + " guesses left")
            guessed_letters.append(user_input)
        if user_input in word and user_input in guessed_letters:
            guesses -= 1


    # coding
    if word == "coding":
        if user_input == "c":
            coding[0] = "c"
            guessed_letters.append(user_input)
            guesses += 1
            print_coding()
        elif user_input == "o":
            coding[1] = "o"
            guessed_letters.append(user_input)
            guesses += 1
            print_coding()
        elif user_input == "d":
            coding[2] = "d"
            guesses += 1
            guessed_letters.append(user_input)
            print_coding()
        elif user_input == "i":
            coding[3] = "i"
            guesses += 1
            guessed_letters.append(user_input)
            print_coding()
        elif user_input == "n":
            coding[4] = "n"
            guesses += 1
            guessed_letters.append(user_input)
            print_coding()
        elif user_input == "g":
            coding[5] = "g"
            guessed_letters.append(user_input)
            guesses += 1
            print_coding()
        elif user_input not in word and user_input not in guessed_letters and user_input.isalpha() and len(user_input) == 1:
            print(user_input + " is not in the word")
            print("you have " + str(chances) + " guesses left")
            guessed_letters.append(user_input)
        if user_input in word and user_input in guessed_letters:
            guesses -= 1


    # pain
    if word == "pain":
        if user_input == "p":
            pain[0] = "p"
            guesses += 1
            guessed_letters.append(user_input)
            print_pain()
        elif user_input == "a":
            pain[1] = "a"
            guesses += 1
            guessed_letters.append(user_input)
            print_pain()
        elif user_input == "i":
            pain[2] = "i"
            guesses += 1
            guessed_letters.append(user_input)
            print_pain()
        elif user_input == "n":
            pain[3] = "n"
            guesses += 1
            guessed_letters.append(user_input)
            print_pain()
        elif user_input not in word and user_input not in guessed_letters and user_input.isalpha() and len(user_input) == 1:
            print(user_input + " is not in the word")
            print("you have " + str(chances) + " guesses left")
            guessed_letters.append(user_input)
        if user_input in word and user_input in guessed_letters:
            guesses -= 1

    # checking the game
    if guesses == len(word):
        print("you got the word, you win")
        break
    if chances == 0:
        print("you lose. the word was " + word)
        break