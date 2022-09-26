print("this program will guess your number in the range of 20")
print("give me 5 hints and 5 chances to guess your number")

user = input(
    "enter your number which i'll be guessing (don't worry i wont know your number until i actually guess your number): ")

cool = False

while True:

    if not user.isnumeric():
        print("invalid input. please enter a number between 1 to 20")
        user = input(
            "enter your number which i'll be guessing: ")
    elif user.isnumeric():
        user = int(user)

        if int(user) < 1 or int(user) > 20:
            print("invalid input. please enter a number between 1 to 20")
            user = input(
                "enter your number which i'll be guessing: ")
        else:
            cool = True
            break


hints = 7
guess = 20
if cool is True:
    print("my first guess is 20")
    while True:

        if hints == 7:
            hint = input("your hint (enter \"higher\" or \"lower\". if i got it right, enter \"cool\"): ")
            if hint == "lower":
                guess = guess / 2
                print("ok now my guess is " + str(guess))
                print("")
                hints = hints - 1
            elif hint == "higher":
                print("nah you trippin, your number is surely under 20")
                print("")
            elif hint == "cool":
                print("hell yea im so pro B)")
                break
            else:
                print("i dont understand your hint")
                print("")

        if hints == 6:
            hint = input("your hint (enter \"higher\" or \"lower\". if i got it right, enter \"cool\"): ")
            if hint == "lower":
                guess = guess / 2
                print("ok now my guess is " + str(guess))
                print("")
                hints = hints - 1
            elif hint == "higher":
                guess = guess + (guess / 2)
                print("ok now my guess is " + str(guess))
                print("")
                hints = hints - 1
            elif hint == "cool":
                print("hell yea im so pro B)")
                break
            else:
                print("i dont understand your hint")
                print("")

        if hints == 5:
            hint = input("your hint (enter \"higher\" or \"lower\". if i got it right, enter \"cool\"): ")
            if hint == "lower":
                guess = guess - 2
                print("ok now my guess is " + str(guess))
                print("")
                hints = hints - 1
            elif hint == "higher":
                guess = guess + 3
                print("ok now my guess is " + str(guess))
                print("")
                hints = hints - 1
            elif hint == "cool":
                print("hell yea im so pro B)")
                break
            else:
                print("i dont understand your hint")
                print("")

        if hints == 4:
            hint = input("your hint (enter \"higher\" or \"lower\". if i got it right, enter \"cool\"): ")
            if hint == "lower":
                guess = guess - 1
                print("ok now my guess is " + str(guess))
                print("")
                hints = hints - 1
            elif hint == "higher":
                guess = guess + 1
                print("ok now my guess is " + str(guess))
                print("")
                hints = hints - 1
            elif hint == "cool":
                print("hell yea im so pro B)")
                break
            else:
                print("i dont understand your hint")
                print("")

        if hints == 3:
            hint = input("your hint (enter \"higher\" or \"lower\". if i got it right, enter \"cool\"): ")
            if hint == "lower":
                guess = guess - 1
                print("ok now my guess is " + str(guess))
                print("")
                hints = hints - 1
            elif hint == "higher":
                print("theres no way it can be higher, quit lying bruh. unless you're really stupid")
                print("your number is " + str(user) + " and my guess was " + str(user) + ". (╯▔皿▔)╯")
                break
            elif hint == "cool":
                print("hell yea im so pro B)")
                break
            else:
                print("i dont understand your hint")
                print("")

        if hints == 2:
            result = input("so did i got it right? (yes/no): ")
            if result == "yes":
                print("ez ez, im so cool B)")
                break
            if result == "no":
                if guess != user:
                    print("your number was actually " + str(user))
                    print("bruh you were giving me wrong hints what the fuck is wrong with you")
                    break
                elif guess == user:
                    print("theres no way i got that wrong, quit lying bruh. unless you're really stupid")
                    print("your number is " + str(user) + " and my guess was " + str(user) + ". (╯▔皿▔)╯")
                    break