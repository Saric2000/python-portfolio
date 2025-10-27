import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL of shop page
url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select(".product_pod")

data = []
for book in books:
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text.strip()
    data.append({"Title": title, "Price": price})

df = pd.DataFrame(data)
df["Date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
df.to_excel("book_prices.xlsx", index=False)

print("Saved book_prices.xlsx successfully!")
