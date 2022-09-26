import random

print("welcome to a number guessing game")
print("guess a number between 1 to 20")
print("you have 7 guesses")

limit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

guesses = 0

number = random.choice(limit)

while True:
    guess = input("enter your guess: ")
    print("\n")

    cool = False

    if not guess.isnumeric():
        print("invalid input, please enter a number")
        print("\n")
    else:
        guess = int(guess)
        cool = True

    if cool is True:
        if 20 < guess < 1:
            print("your guess is out of bounds. the limit is between 1 and 20")

        if guess > number:
            print("the actual number is lower than your guess, try again")
            guesses += 1
            print("you have " + str(7 - guesses) + " guesses left")
            print("\n")
        elif guess < number:
            print("the actual number is higher than your guess, try again")
            guesses += 1
            print("you have " + str(7 - guesses) + " guesses left")
            print("\n")
        elif guess == number:
            print("you won sheeesh")
            break

        if guesses == 7:
            print("you're out of guesses, you lost :(")
            print("the actual number is " + str(number))