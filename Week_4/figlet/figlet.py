import sys
from pyfiglet import Figlet

if len(sys.argv) == 1:
    font = "standard"
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        font = sys.argv[2]
    else:
        sys.exit("Invalid arguments")
else:
    sys.exit("Invalid number of arguments")

try:
    f = Figlet(font=font)
except:
    sys.exit("Invalid font")
else:
    text = input("Input: ")
    print("Output:")
    print(f.renderText(text))
