user_input = input("File name: ").strip().lower()
split = user_input.split(".")
size = len(split)

split2 = split[size-1].replace("jpg", "jpeg").replace("txt", "plain")

if size < 2:
    type = "application"
    split2 = "octet-stream"
else:
    match split[size-1]:
        case "gif" | "jpg" | "jpeg" | "png":
            type = "image"
        case "txt":
            type = "text"
        case "pdf" | "zip":
            type = "application"
        case _:
            type = "application"
            split2 = "octet-stream"

print(f"{type}" + "/" + f"{split2}")
