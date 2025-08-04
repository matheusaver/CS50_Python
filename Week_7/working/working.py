import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM)? to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)?$", s):
        if int(time.group(1)) > 12 or int(time.group(4)) > 12:
            raise ValueError
        start = check_hour(int(time.group(1)), time.group(2), time.group(3))
        finish = check_hour(int(time.group(4)), time.group(5), time.group(6))
        return start + " to " + finish
    else:
        raise ValueError


def check_hour(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if not hour == 12:
            hour += 12

    if minute == None:
        minute = ":00"
        format = f"{hour:02}{minute:02}"

    else:
        format = f"{hour:02}:{minute:02}"

    return format


if __name__ == "__main__":
    main()
