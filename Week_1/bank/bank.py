user_input = input("Greeting: ").strip().lower()
split = user_input.split()[0]
split2 = ''.join(filter(str.isalpha, split))
if split2 == "hello":
    print("$0")
elif split2[0] == "h":
    print("$20")
else:
    print("$100")
