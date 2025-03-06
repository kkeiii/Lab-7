import requests
import json
import time

#1
def get_weather(city_name, api_key):
    url_weather = "https://api.openweathermap.org/data/2.5/weather"
    parametrs = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
        "lang": "ru"
    }
    

    response = requests.get(url_weather, params=parametrs)
    if response.status_code == 200:
        data = response.json()
        

        weather_info = {
            "Город": data["name"],
            "Температура": f"{data['main']['temp']} °C", 
            "По ощущениям": f"{data['main']['feels_like']} °C",
            "Погода": data['weather'][0]['description'].capitalize(),
            "Влажность": f"{data['main']['humidity']}%",
            "Давление": f"{data['main']['pressure']} hPa",
        }
        
        
        for key, value in weather_info.items():
            print(f"{key}: {value}")
    else:
        print("Ошибка, проверьте данные")


if __name__ == "__main__":
    API_KEY = "cd71d9ca20d0b9cb8b08fdbb62e98d41"
    CITY = "Уфа"
    get_weather(CITY, API_KEY)


time.sleep(2)
print()
#2
def word_info(word):
    url_words = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url_words)
    
    if response.status_code == 200:
        data = response.json()[0]
        
        word_info = {
            "word": data["word"],
            "phonetics": data.get("phonetics", [{}])[0].get("text", "no data"),
            "definition": data["meanings"][0]["definitions"][0]["definition"],
            "example": data["meanings"][0]["definitions"][0].get("example", "no example"),
            "synonyms": ", ".join(data["meanings"][0]["definitions"][0].get("synonyms", ["no data"])),
            "antonyms": ", ".join(data["meanings"][0]["definitions"][0].get("antonyms", ["no data"]))
        }
        
        for key, value in word_info.items():
            print(f"{key}: {value}")
    else:
        print("Error: word not found or request is incorrect.")

if __name__ == "__main__":
    word = input("Enter the word: ")
    word_info(word)


