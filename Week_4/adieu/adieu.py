import sys
name_list = []

while True:
    try:
        user_input = input("Name: ")
        name_list.append(user_input)
    except EOFError:
        break

people = len(name_list)
i = 0

print()
print("Adieu, adieu, to ", end="")

if people == 1:
    print(name_list[0])
    sys.exit()
elif people == 2:
    print(f"{name_list[0]} and {name_list[1]}")
    sys.exit()
else:
    for i in range(people):
        if people == (i+1):
            print(f"and {name_list[i]}")
            sys.exit()
        else:
            print(f"{name_list[i]}, ", end="")
            i += 1
