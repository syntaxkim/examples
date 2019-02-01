import requests
import json

def get_coordinates(city):
    r = requests.get("https://darksky.net/geo", params={'q':city})

    if r.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")

    coordinates = r.json()

    latitude = f"{coordinates['latitude']:.2f}"
    longitude = f"{coordinates['longitude']:.2f}"

    return latitude, longitude

if __name__ == "__main__":
    city = input("city: ")
    latitude, longitude = get_coordinates(city)

    print(latitude, longitude)
