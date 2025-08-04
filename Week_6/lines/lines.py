import sys
count_lines = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except (FileNotFoundError):
    sys.exit("File does not exist")
else:
    for line in lines:
        line = line.lstrip()
        if line.startswith("#"):
            continue
        elif line == "":
            continue
        else:
            count_lines +=1
print(count_lines)
