def main():
    user_input = input("Greeting: ").strip().lower()
    split = user_input.split()[0]
    print(f"${value(split)}")


def value(greeting):
    if greeting == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
