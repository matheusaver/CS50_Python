def main():
    user_input = input("camelCase: ")
    convert(user_input)

def convert(str):
    for char in str:
        if char.isupper():
            print("_" + char.lower(), end="")
        else:
            print(char, end="")
    print()

if __name__ == "__main__":
    main()
