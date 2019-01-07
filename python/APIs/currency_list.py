import requests

def main():
    res = requests.get("https://api.exchangeratesapi.io/latest")

    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
        
    data = res.json()

    currency_list = []

    for k in data['rates']:
        currency_list.append(k)
    
    print(data)

    print(currency_list)

if __name__ == "__main__":
    main()  
    