import random

number = 1

def main():
    level = user_input("Level: ")
    if level > 1:
        global number
        number = random.randint(1, level)
    guessing()


def guessing():
    while True:
        guess = user_input("Guess: ")
        if guess < number:
            print("Too small!")
            continue
        elif guess > number:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break


def user_input(txt):
    while True:
        try:
            user_input = int(input(txt))
            if user_input < 1:
                continue
            else:
                return user_input
        except:
            pass


if __name__ == "__main__":
    main()
