import requests
import json, os

def main():
    secret_key = os.getenv("SECRET_KEY")

    res = requests.get(f"https://api.darksky.net/forecast/{secret_key}/37.532600,127.024612",
        params={"units": "si", "exclude": "minutes,hourly,daily,alerts,flags"})

    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")

    data = res.json()
    summary = data["currently"]["summary"]

    print(res)
    print(summary)

    with open("darksky.json", "w") as f:
        f.write(json.dumps(res.json(), indent=4))
    
if __name__ == "__main__":
    main()