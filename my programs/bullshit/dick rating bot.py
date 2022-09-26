import random
sizes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

dick = ["ε", "", "D"]

def print_dick():
    for parts in dick:
        print(parts, end="")
    print("\n")

while True:
    useable = False
    user = input("want me to rate your dick? (yes/no): ")
    if user == "yes":
        useable = True
    elif user == "no":
        print("hah, bet you got a small dick and you already know it")
        break
    else:
        print("bruh, yes or no man?")

    if useable == True:
        size = random.choice(sizes)
        size = int(size)

        if size == 0:
            print("what the fuck, you should go to the doctor's and get it checked bro")
        elif 1 <= size <= 4:
            print("lol tiny dick like what the fuck")
        elif 5 <= size <= 7:
            print("okay pretty average, not bad at all")
        elif 8 <= size <= 9:
            print("woahhh, huge dick bro")
        elif size == 10:
            print("HOLY FUCKING SHIT WHAT THE FUCK MAGNUM DICK GODDAMN")

        dick[1] = ("=" * size)

        print_dick()
        break