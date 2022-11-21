inp = input("number of cases: ")
cases = 0
case = 1
while True:
    if inp.isdigit():
        cases = int(inp)
        break
    else:
        cases = input("number of cases must be a whole number: ")

while cases > 0:
    in1 = input("the range of houses (100 max): ")
    in2 = input("your budget (100k max): ")
    print()
    num_of_houses = 0
    budget = 0
    affordable = 0
    prices = []
    while True:
        if in1.isdigit() and 1 <= int(in1) <= 100 and in2.isdigit() and 1 <= int(in2) <= 100000:
            num_of_houses = int(in1)
            budget = int(in2)
            break
        else:
            in1 = input("the range of houses must be a whole number over 1 and under 100: ")
            in2 = input("your budget must be a whole number over 1 and under 100k: ")
            print()



    while num_of_houses > 0:
        print("enter the prices of each houses (each house costs 1k max)")
        in3 = input("the prices: ")
        print()

        while True:
            if in3.isdigit() and 1 <= int(in3) <= 1000:
                prices.append(in3)
                break
            else:
                in3 = input("the prices of the houses must be a number under 1k: ")
                print()

        num_of_houses = num_of_houses - 1


    prices = [int(x) for x in prices]
    prices.sort()
    for i in range(len(prices)):
        budget = budget - int(prices[i])
        if budget >= 0:
            affordable += 1
        elif budget < 0:
            pass

    print()
    print("case #" + str(case) + ": " + str(affordable))

    case += 1
    cases -= 1