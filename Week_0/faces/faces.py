def convert(input):
    return input.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input("Enter your text here: ")
    print(convert(user_input))

main()
