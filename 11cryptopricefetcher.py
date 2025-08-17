# This is an app for checking the most current crypto price for different coins

import requests
import time


print("Welcome to the Crypto Price Fetcher App")
print("Bringing to you the most currrent crypto prices")
print("\n")


def get_crypto_price(coin_ids, currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(coin_ids),
        "vs_currencies": currency
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None


# List of popular coins
popular_coins = ["bitcoin", "ethereum", "dogecoin", "solana", "cardano"]

user_choice = input(
    "Enter the coin name you are searching for (e.g., bitcoin) or 'all' for all major coins: ").strip().lower()
currency_choice = input(
    "Enter the currency (e.g., usd, eur, ngn): ").strip().lower()

if user_choice == "all":
    coins = popular_coins
else:
    coins = [user_choice]

prices = get_crypto_price(coins, currency_choice)
if prices:
    for coin in coins:
        price = prices.get(coin, {}).get(currency_choice)
        if price is not None:
            print(
                f"The price of {coin} is {price:,.2f} {currency_choice.upper()}")
        else:
            print(f"Price for {coin} not found.")

print("Updating in 30 seconds...\n")
time.sleep(30)
