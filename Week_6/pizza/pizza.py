import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        table = csv.DictReader(file)
        print(tabulate(table, headers="keys", tablefmt="grid"))
except (FileNotFoundError):
    sys.exit("File does not exist")
