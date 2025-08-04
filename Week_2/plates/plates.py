def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if lenght(s) and twoletters(s) and alphanumeric(s) and numbers(s):
        return True
    else:
        return False

def lenght(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True

def twoletters(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False

def alphanumeric(s):
    if s.isalnum():
        return True
    else:
        return False

def numbers(s):
    i = 0
    while i < len(s) - 1:
        if not s[i].isalpha():
            if s[i] == "0":
                return False
            elif not s[i:].isdigit():
                return False
            else:
                return True
        i += 1
    return True


main()
