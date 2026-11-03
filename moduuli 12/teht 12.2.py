
import requests

# Oma OpenWeather API-avain
api_key = "OMA_API_AVAIN"

# Kysytään käyttäjältä paikkakunta
city = input("Anna paikkakunta: ")

# Rajapinnan osoite ja parametrit
url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric",
    "lang": "fi"
}

# Haetaan säätiedot
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Haetaan säätilan kuvaus ja lämpötila
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    # Tulostetaan tiedot
    print("Säätila:", weather)
    print("Lämpötila:", temperature, "°C")

else:
    print("Säätietojen hakeminen epäonnistui.")
