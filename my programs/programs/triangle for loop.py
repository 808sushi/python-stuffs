while True:
    useable = False
    user_input = input("enter the height of your pyramid or enter 0 to quit: ")

    if not user_input.isnumeric():
        print("please type a number")
    else:
        useable = True

    if user_input == "0":
        break

    if useable == True:
        height = int(user_input)
        for i in range(height):
            for o in range(height - i - 1):
                print("  ", end="")
            for o in range(i + 1):
                print("[]", end="")
            for o in range(1):
                print(" ", end="")
            for o in range(i + 1):
                print("[]", end="")

            print(" ")