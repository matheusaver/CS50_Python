import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_address = re.fullmatch(r"([\d]+)+\.+([\d]+)+\.+([\d]+)+\.+([\d]+)", ip)
    if ip_address:
        if ip_address.group() == "127.0.0.1":
            return True
        else:
            first, second, third, fourth = ip.split(".")
            if (range(first) and range(second) and range(third) and range(fourth)):
                return True
            else:
                return False
    else:
        return False

def range(number):
    if 1 <= int(number) <= 255:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
