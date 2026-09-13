def hangman():
    import random
    words = ("apple","orange","banana","coconut","pineapple")
    word  = random.choice(words)
    word_list = list(word)
    replacer = []
    for char in word:
        replacer.append("_")
    unique_word_set = set(word_list)
    attempts = len(unique_word_set)+2

    while attempts!=0:
        print(" ".join(replacer))
        user = input("\n")
        user = user.lower()
        if user in word_list:
            for i in range(len(word_list)):
                if word_list[i] == user:
                    replacer[i] = user

        if replacer == word_list:
            print(" ".join(replacer))
            print("You Won!")
            break

        attempts-=1

        if attempts == 0 and replacer != word_list:
            print("Attempts Over! You lost!")

def main():
    print("Welcome to the Hangman Game (To continue press any E , Q to quit)")
    user_res = input("\n")
    is_running = False
    if user_res == "E" :
        is_running = True
    else:
        print("Thank You for your Time!")
    while is_running:

        print("-------------------HANGMAN GAME-------------------")
        hangman()
        user_res2 = input("Do you wish to continue (Y/N)")
        if user_res2 != "Y":
            print("Thank You for Playing!")
            is_running = False


if __name__ == "__main__":
    main()