import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        api_key = "YourApiKeyHere"  # 🔁 Replace with your real CoinCap API key
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get("https://api.coincap.io/v3/assets/bitcoin", headers=headers)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
        total = bitcoins * price
        print(f"${total:,.4f}")
    except requests.RequestException:
        sys.exit("Error: Could not fetch Bitcoin price")

if __name__ == "__main__":
    main()
