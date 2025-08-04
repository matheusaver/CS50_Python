import sys


def main():
    user_input = input("Fraction: ")
    percent = convert(user_input)
    gauge(percent)


def convert(fraction):
    user_input = fraction.split("/")
    try:
        percentage = (int(user_input[0]) / int(user_input[1])) * 100
   # except (ValueError, ZeroDivisionError):
   #     sys.exit(1)
    else:
        return percentage


def gauge(percentage):
    if 0.0 <= percentage <= 1.0:
        print("E")
    elif 1.0 < percentage < 99.0:
        print(f"{round(percentage)}%")
    elif 99.0 <= percentage <= 100.0:
        print("F")


if __name__ == "__main__":
    main()
