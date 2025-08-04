import random

TOTAL_PROBLEMS = 10

def main():
    level = get_level()
    score = 0
    for _ in range(TOTAL_PROBLEMS):
        number1 = generate_integer(level)
        number2 = generate_integer(level)
        answer = number1 + number2
        attempts = 0
        while attempts < 3:
            response = int(input(f"{number1} + {number2} = "))
            if response == answer:
                score = score + 1
                break
            else:
                print("EEE")
                attempts = attempts + 1
        if attempts == 3:
            print(f"{number1} + {number2} = {answer}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            user_input = int(input("Level: "))
            if user_input >= 1 and user_input <= 3:
                return user_input
        except:
            pass


def generate_integer(level):
    if level == 1:
        ranges = [0, 9]
    elif level == 2:
        ranges = [10, 99]
    else:
        ranges = [100, 999]
    return random.randint(ranges[0], ranges[1])


if __name__ == "__main__":
    main()
