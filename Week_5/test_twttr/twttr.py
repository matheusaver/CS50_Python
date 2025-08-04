#CONST_VOWELS = "aeiou"
CONST_VOWELS = "aeiouAEIOU"

def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(word):
    short = ""
    for char in word:
        if char in CONST_VOWELS:
            continue
        else:
            short = short + char
    return short


if __name__ == "__main__":
    main()
