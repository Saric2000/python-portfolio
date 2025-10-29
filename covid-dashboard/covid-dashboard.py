import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

url = "https://disease.sh/v3/covid-19/countries"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
df = df[["country", "cases", "todayCases", "deaths", "todayDeaths", "recovered", "active"]]

top_countries = df.sort_values(by="cases", ascending=False).head(10)

plt.figure(figsize=(10, 6))
bars = plt.bar(top_countries["country"], top_countries["cases"], color="#4a90e2", alpha=0.8)
plt.title("Top 10 Countries by COVID-19 Cases", fontsize=14, weight="bold")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 50000, f"{int(yval):,}", ha="center", va="bottom", fontsize=8)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
bars = plt.bar(top_countries["country"], top_countries["deaths"], color="#e94e77", alpha=0.8)
plt.title("Top 10 Countries by COVID-19 Deaths", fontsize=14, weight="bold")
plt.xlabel("Country")
plt.ylabel("Total Deaths")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5000, f"{int(yval):,}", ha="center", va="bottom", fontsize=8)

plt.tight_layout()
plt.show()

df.to_csv("covid-dashboard/covid_data.csv", index=False)
print("Data saved to covid-dashboard/covid_data.csv")
