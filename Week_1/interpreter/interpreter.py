user_input = input("Expression: ")
split = user_input.split()

match split[1]:
    case "/":
        result = (int(split[0]) / int(split[2]))
        print("{:.1f}".format(result))
    case "*":
        result = (int(split[0]) * int(split[2]))
        print("{:.1f}".format(result))
    case "+":
        result = (int(split[0]) + int(split[2]))
        print("{:.1f}".format(result))
    case "-":
        result = (int(split[0]) - int(split[2]))
        print("{:.1f}".format(result))
