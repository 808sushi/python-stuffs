print("")
print("make sure to end your paragraph with '.' '?' or '!' \n")

while True:
    user = input("your shit (\"q\" to quit): ")

    if user == "q":
        print("ok cool")
        break

    letters_len = len(user) - user.count(" ") - user.count(",") - user.count(";") - user.count("'") - user.count(".") - user.count("?") - user.count("!")

    word_list = user.split()
    words_len = len(word_list)

    sentence_len = 0
    for i in user:
        if i == ".":
            sentence_len += 1

        if i == "?":
            sentence_len += 1

        if i == "!":
            sentence_len += 1

    Coleman_Liau = 0.0588 * letters_len / words_len * 100 - 0.296 * sentence_len / words_len * 100 - 15.8
    result = round(Coleman_Liau)

    if result > 16:
        print("your shit is grade 16+ \n")
        print("")
    elif result < 1:
        print("your shit is before grade 1 \n")
    else:
        print("your shit is grade " + str(result), "\n")