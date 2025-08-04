def convert(input):
    return input * (300000000 ** 2)

def main():
    user_input = int(input("Enter the mass in kg: "))
    print(convert(user_input))

main()
