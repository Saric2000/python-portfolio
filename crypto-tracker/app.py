import requests
import pandas as pd

coins = ["bitcoin", "ethereum", "dogecoin", "litecoin", "cardano", "solana","pi-network"]

url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies=usd"

response = requests.get(url).json()

data = []
for coin in coins:
    if coin in response:
        data.append({
            "Coin": coin.capitalize(),
            "Price (USD)": response[coin]["usd"]
        })
    else:
        data.append({
            "Coin": coin.capitalize(),
            "Price (USD)": "N/A"
        })

df = pd.DataFrame(data)
df.to_csv("crypto-tracker/crypto_prices.csv", index=False)
print("Crypto prices saved to crypto-tracker/crypto_prices.csv")
