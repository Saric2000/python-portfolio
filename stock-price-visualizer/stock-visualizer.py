import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

stocks = ["AAPL", "TSLA", "MSFT", "GOOGL"]

end_date = datetime.now()
start_date = end_date - timedelta(days=30)

data = yf.download(stocks, start=start_date, end=end_date)

if ("Adj Close" in data.columns.get_level_values(0)):
    data = data["Adj Close"]
else:
    data = data["Close"]


print("Downloaded data:")
print(data.tail())


plt.figure(figsize=(12, 6))
for stock in stocks:
    plt.plot(data.index, data[stock], label=stock)

plt.title("Stock Price Movement (Last 30 Days)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

data.to_csv("stock-price-visualizer/stock_prices.csv")
print("Data saved to stock-price-visualizer/stock_prices.csv")
