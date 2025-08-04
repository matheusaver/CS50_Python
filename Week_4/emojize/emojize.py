import emoji

emoji_code = input("Input: ")
output = emoji.emojize(emoji_code, language="alias")
print(f"Output: {output}")
