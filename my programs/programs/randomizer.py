import random

print("this is a randomizer")
print()
print("input (1) if you want to pick between 2 numbers of your choice")
print("input (2) if you want to pick between random choices of your creation")
print("input (0) to end this program")
print()

while True:

    user = input("mode: ")
    print()

    choices = []

    if user == "0":
        print("program ended. have a nice day")
        break
    elif user == "1":
        while True:
            first = input("your starting number: ")
            last = input("your end number: ")
            print()

            if first.isnumeric() and last.isnumeric():
                first = int(first)
                last = int(last)

                if first < last:
                    for i in range(first, last):
                        choices.append(i)
                    r = random.choice(choices)
                    print("the range is from " + str(first) + " to " + str(last))
                    print("the randomized choice is: " + str(r))
                    print()
                    break
                else:
                    print("your starting number must be lower than your end number")
                    print()

            else:
                print("invalid input. please enter a whole number only")
                print()
    elif user == "2":
        while True:
            word = input("your whatever choice ('0' if you have no more inputs): ")
            print()

            if word == "0":
                break
            else:
                choices.append(word)

            r = random.choice(choices)
            print("the given inputs are: ")
            print(', '.join(choices))
            print()
            print("the randomized choice is: " + r)
            print()

    else:
        print("invalid input")
        print()