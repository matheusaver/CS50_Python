import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    repetitions = len(re.findall(r"\bum\b", s, re.I))
    if repetitions:
        return int(repetitions)
    else:
        return 0


if __name__ == "__main__":
    main()
