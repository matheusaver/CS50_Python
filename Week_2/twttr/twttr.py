CONST_VOWELS = "aeiouAEIOU"

def main():
    user_input = input("Input: ")
    remove_vowel(user_input)

def remove_vowel(string):
    for char in string:
        if char in CONST_VOWELS:
            continue
        else:
            print(char, end="")
    print()

if __name__ == "__main__":
    main()
