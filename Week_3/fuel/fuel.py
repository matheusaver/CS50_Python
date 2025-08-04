while True:
    try:
        user_input = input("Fraction: ").split("/")
        percentage = (int(user_input[0]) / int(user_input[1])) * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if 0.0 <= percentage <= 1.0:
            print("E")
            break
        elif 1.0 < percentage < 99.0:
            print(f"{round(percentage)}%")
            break
        elif 99.0 <= percentage <= 100.0:
            print("F")
            break
        else:
            continue

