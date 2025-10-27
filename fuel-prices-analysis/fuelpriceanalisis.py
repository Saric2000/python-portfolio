import pandas as pd
import matplotlib.pyplot as plt

 #Make test CSV if not exist
'''data = {
    "Date": pd.date_range("2025-10-01", periods=10, freq="D"),
    "Gasoline": [1.65, 1.67, 1.64, 1.68, 1.7, 1.69, 1.72, 1.74, 1.71, 1.73],
    "Diesel": [1.55, 1.57, 1.54, 1.58, 1.6, 1.59, 1.62, 1.63, 1.61, 1.65],
}
df = pd.DataFrame(data)
df.to_csv("fuel_prices.csv", index=False)'''

df = pd.read_csv("fuel_prices.csv")

print("Average Gasoline:", df["Gasoline"].mean())
print("Max Diesel:", df["Diesel"].max())

plt.plot(df["Date"], df["Gasoline"], label="Gasoline")
plt.plot(df["Date"], df["Diesel"], label="Diesel")
plt.legend()
plt.title("Fuel Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price (€/L)")
plt.show()
