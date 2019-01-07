import requests
import json

def main():
    res = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=EUR")

    # Very often, you should check if the request was OK when you're writing code that uses APIs.
    if res.status_code != 200:
        # If something bad happens, quit the program.
        raise Exception("ERROR: API request unsuccessful.")
    
    print(f"{'res':16} ==> {res}")
    print(f"{'res.json()':16} ==> {res.json()}")
    print(f"{'res.status_code':16} ==> {res.status_code}")

    # data would be like {'base': 'USD', 'date': '2018-10-02', 'rates': {'EUR': 0.8663259118}}    
    data = res.json()
    rate = data["rates"]["EUR"]
    
    # print only the data I need
    print(f"1 USD is equal to {rate} EUR")

    # Create a json file which contains the data of the response.
    # open is a Python's built-in function that gets a file object.
    # In Python, a file is categorized as either text or binary.
    with open("currency0.json", "w") as f:
        # json.dumps serializes an object to a JSON formatted str.
        # You can't write res.json() because it is dict not str.
        # indent is an optional argument for pretty printing.
        data = json.dumps(res.json(), indent=4)
        # You can write res.text instead.
        f.write(data)

if __name__ == "__main__":
    main()