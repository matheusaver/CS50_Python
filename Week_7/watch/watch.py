import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r"youtube\.com/embed/(\w+).+</iframe>$", s)
    if url:
        return(f"https://youtu.be/" + url.group(1))
    else:
        return None


if __name__ == "__main__":
    main()
