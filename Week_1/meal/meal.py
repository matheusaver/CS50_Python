def main():
    user_input = input("What time is it? ")
    time = convert(user_input)
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    return (float(hours) + (float(minutes) / 60))

if __name__ == "__main__":
    main()








