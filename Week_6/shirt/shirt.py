import sys
import os
from PIL import Image
from PIL import ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(('jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG')):
    sys.exit("Invalid input")
input_extension = os.path.splitext(sys.argv[1])
output_extension = os.path.splitext(sys.argv[2])
if input_extension[1] != output_extension[1]:
    sys.exit("Input and output have different extensions")


try:
    before = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
except (FileNotFoundError):
    sys.exit(f"Could not found {sys.argv[1]}")


shirt_size = shirt.size
before = ImageOps.fit(before, shirt_size)
before.paste(shirt, box = (0, 0), mask = shirt)
before.save(sys.argv[2], format=None)
