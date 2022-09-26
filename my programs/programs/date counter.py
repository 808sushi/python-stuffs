from datetime import *

print("this is a date countdown program. \n")

today = date.today()

fr = today.strftime("%d/%m/%Y")

print("today is ", fr, "\n")

date = int(input("enter future date: "))
month = int(input("enter future month: "))
year = int(input("enter future year: "))
print("\n")

while True:
    if 31 >= date < int(today.day):
        if int(today.month) == 1 or int(today.month) == 3 or int(today.month) == 5 or int(today.month) == 7 or int(today.month) == 8 or int(today.month) == 10 or int(today.month) == 12:
            counter_day_31 = 31 + date - int(today.day)
            print("the event will happen in: ")
            print(str(counter_day_31) + " day(s)")
        elif int(today.month) == 4 or int(today.month) == 6 or int(today.month) == 9 or int(today.month) == 11:
            counter_day_30 = 30 + date - int(today.day)
            print("the event will happen in: ")
            print(str(counter_day_30) + " day(s)")
        elif int(today.month) == 2:
            counter_day_29 = 29 + date - int(today.day)
            print("the event will happen in: ")
            print(str(counter_day_29) + " day(s)")
    if 31 >= date > int(today.day):
        counter_day = date - int(today.day)
        print("the event will happen in: ")
        print(str(counter_day) + " day(s)")
    if date > 31:
        print("invalid date")
        break


    if 12 >= month < int(today.month) and date > int(today.day):
        counter_month_s = 12 + month - int(today.month)
        print(str(counter_month_s) + " month(s)")
    elif 12 >= month > int(today.month) and date > int(today.day):
        counter_month_l = month - int(today.month)
        print(str(counter_month_l) + " month(s)")
    elif 12 >= month < int(today.month) and date < int(today.day):
        counter_month_s = 12 + month - int(today.month) - 1
        print(str(counter_month_s) + " month(s)")
    elif 12 >= month > int(today.month) and date < int(today.day):
        counter_month_l = month - int(today.month) - 1
        print(str(counter_month_l) + " month(s)")
    elif 12 < month:
        print("invalid month")
        break


    if year >= int(today.year):
        counter_year = year - int(today.year)
        print(str(counter_year) + " year(s)")
    elif year < int(today.year):
        print("invalid year")
        break

    break
'''this is an unfinished program'''