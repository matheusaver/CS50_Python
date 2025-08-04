import json
import requests
import sys
key = 0 #INSERT YOUR KEY FROM COINCAP HERE

if len(sys.argv) != 2:
    sys.exit("Invalid arguments")


try:
    user_input = float(sys.argv[1])
except:
    sys.exit("Invalid value")


try:
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {
        "Authorization": "Bearer {key}"
    }
    response = requests.get(url, headers=headers)
except requests.RequestException:
    sys.exit("Error")

table = response.json()
amount = float(table["data"]["priceUsd"]) * user_input
print(f"${amount:,.4f}")
