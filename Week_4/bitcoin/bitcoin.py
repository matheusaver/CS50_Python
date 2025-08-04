import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Invalid arguments")


try:
    user_input = float(sys.argv[1])
except:
    sys.exit("Invalid value")


try:
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {
        "Authorization": "Bearer 3d19b2507708544ba82a48acc7d610eb882bb7643c7591a6e03f531165d181f8"
    }
    response = requests.get(url, headers=headers)
except requests.RequestException:
    sys.exit("Error")

table = response.json()
amount = float(table["data"]["priceUsd"]) * user_input
print(f"${amount:,.4f}")
