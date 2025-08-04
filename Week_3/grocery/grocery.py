from collections import OrderedDict

item_list = {}

while True:
    try:
        user_input = input().upper()
        if user_input in item_list:
            item_list[user_input] = item_list[user_input] + 1
        else:
            item_list[user_input] = 1
    except EOFError:
        break

ordered_dict = OrderedDict(sorted(item_list.items(), key=lambda t: t[0]))

for name in ordered_dict:
    print(f"{ordered_dict[name]} {name}")

