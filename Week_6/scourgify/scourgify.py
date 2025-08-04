import sys
import csv
output = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        table = csv.DictReader(file)
        for row in table:
            full_name, house = row["name"], row["house"]
            last, first = full_name.rstrip().split(",")
            output.append({"first": first.strip(), "last": last.strip(), "house": house})

except (FileNotFoundError):
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as file:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(output)
