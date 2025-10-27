import requests
from bs4 import BeautifulSoup
import pandas as pd
import unidecode

cities = [
    "Bratislava", "Kosice", "Presov", "Nitra", "Zilina", 
    "Poprad", "Piestany", "Prievidza",
]

weather_data = []

for city in cities:
    city_url = unidecode.unidecode(city.lower().replace(" ", "-"))
    url = f"https://www.timeanddate.com/weather/slovakia/{city_url}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    temp_div = soup.find("div", class_="h2")
    condition_p = soup.find("p")
    
    if temp_div and condition_p:
        temp_text = temp_div.text.strip()
        
        if "°F" in temp_text:
            fahrenheit = float(temp_text.replace("\xa0°F", ""))
            temp = round((fahrenheit - 32) * 5/9, 1)
        else:
            temp = float(temp_text.replace("\xa0°C", ""))
        
        condition = condition_p.text.strip()
    else:
        temp = "N/A"
        condition = "N/A"
    
    weather_data.append({
        "City": city,
        "Temperature (°C)": temp,
        "Condition": condition,
        "URL": url
    })

df = pd.DataFrame(weather_data)
df.to_csv("weather-scrapper/weather.csv", index=False)
print("Weather data saved to weather-scrapper/weather.csv")
