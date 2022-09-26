import random
import time

print("welcome to rock, paper, scissors")
print("you'll be playing against the computer \n")

user_wins = 0
com_wins = 0
rounds = 1

while True:
    game = ("rock", "paper", "scissors")
    time.sleep(0.5)
    print("round " + str(rounds) + ":")
    time.sleep(0.5)
    user_input = input("please only pick between 'rock', 'paper' or 'scissors' or type 'q' to quit: ")
    com = random.choice(game)


    #quit
    if user_input == "q" or user_input == "quit":
        print("game ended, have a nice day")
        break


    # draw
    if user_input == com:
        print("you picked: " + user_input)
        time.sleep(0.5)
        print("computer picked: " + com)
        time.sleep(0.5)
        print("its a draw")
        time.sleep(0.5)
        print("you won: " + str(user_wins) + " time(s)")
        time.sleep(0.5)
        print("computer won: " + str(com_wins) + " time(s)")
        rounds += 1
        print("")

    # user wins
    if user_input == "rock" and com == "scissors":
        print("you picked: " + user_input)
        time.sleep(0.5)
        print("computer picked: " + com)
        time.sleep(0.5)
        print("you won")
        time.sleep(0.5)
        user_wins += 1
        print("you won: " + str(user_wins) + " time(s)")
        time.sleep(0.5)
        print("computer won: " + str(com_wins) + " time(s)")
        rounds += 1
        print("")
    elif user_input == "paper" and com == "rock":
        print("you picked: " + user_input)
        time.sleep(0.5)
        print("computer picked: " + com)
        time.sleep(0.5)
        print("you won")
        time.sleep(0.5)
        user_wins += 1
        print("you won: " + str(user_wins) + " time(s)")
        time.sleep(0.5)
        print("computer won: " + str(com_wins) + " time(s)")
        rounds += 1
        print("")
    elif user_input == "scissors" and com == "paper":
        print("you picked: " + user_input)
        time.sleep(0.5)
        print("computer picked: " + com)
        time.sleep(0.5)
        print("you won")
        time.sleep(0.5)
        user_wins += 1
        print("you won: " + str(user_wins) + " time(s)")
        time.sleep(0.5)
        print("computer won: " + str(com_wins) + " time(s)")
        rounds += 1
        print("")

    # com wins
    if user_input == "rock" and com == "paper":
        print("you picked: " + user_input)
        time.sleep(0.5)
        print("computer picked: " + com)
        time.sleep(0.5)
        print("computer won")
        time.sleep(0.5)
        com_wins += 1
        print("you won: " + str(user_wins) + " time(s)")
        time.sleep(0.5)
        print("computer won: " + str(com_wins) + " time(s)")
        rounds += 1
        print("")
    elif user_input == "paper" and com == "scissors":
        print("you picked: " + user_input)
        time.sleep(0.5)
        print("computer picked: " + com)
        time.sleep(0.5)
        print("computer won")
        time.sleep(0.5)
        com_wins += 1
        print("you won: " + str(user_wins) + " time(s)")
        time.sleep(0.5)
        print("computer won: " + str(com_wins) + " time(s)")
        rounds += 1
        print("")
    elif user_input == "scissors" and com == "rock":
        print("you picked: " + user_input)
        time.sleep(0.5)
        print("computer picked: " + com)
        time.sleep(0.5)
        print("computer won")
        time.sleep(0.5)
        com_wins += 1
        print("you won: " + str(user_wins) + " time(s)")
        time.sleep(0.5)
        print("computer won: " + str(com_wins) + " time(s)")
        rounds += 1
        print("")

    #error
    if user_input not in game:
        print("invalid input")
        print("")