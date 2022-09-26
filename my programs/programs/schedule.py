print("this is your week schedule")
schedule = {
    "monday": "7h30 am -> 10 am: korean at school | 3h30 pm -> 5 pm: gym | 6 pm -> 8 pm: tiw class",
    "tuesday": "3h30 pm -> 5 pm: gym",
    "wednesday": "7h30 am -> 10 am: korean at school | 3h30 pm -> 5 pm: gym | 6 pm -> 8 pm: tiw class",
    "thursday": "3h30 pm -> 5 pm: gym",
    "friday": "3h30 pm -> 5 pm: gym | 6 pm -> 8 pm: tiw class",
    "saturday": "3h30 pm -> 5 pm: gym",
    "sunday": "whatever idk do some python or your homework i guess"
}
true = 0
while True:
    user_input = input("which day of the week is it today?: ")
    if user_input.lower() == "monday" or user_input.lower() == "mon":
        print(schedule["monday"])
        true += 1
    elif user_input.lower() == "tuesday" or user_input.lower() == "tue":
        print(schedule["tuesday"])
        true += 1
    elif user_input.lower() == "wednesday" or user_input.lower() == "wed":
        print(schedule["wednesday"])
        true += 1
    elif user_input.lower() == "thursday" or user_input.lower() == "thur":
        print(schedule["thursday"])
        true += 1
    elif user_input.lower() == "friday" or user_input.lower() == "fri":
        print(schedule["friday"])
        true += 1
    elif user_input.lower() == "saturday" or user_input.lower() == "sat":
        print(schedule["saturday"])
        true += 1
    elif user_input.lower() == "sunday" or user_input.lower() == "sun":
        print(schedule["sunday"])
        true += 1
    else:
        print("invalid input")

    if true == 1:
            print("")
            print("program ended, you just need get through this week")
            break
    else:
        continue