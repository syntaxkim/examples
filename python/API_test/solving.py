import requests
import json

def main():
    # GET input (event list)
    r = requests.get("https://api.github.com/repos/rails/rails/events?per_page=100?")

    if r.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
        
    events = r.json()
    
    # Parse users
    USERS = set()
    for event in events:
        USERS.add(event["actor"]["login"])
    users = list(USERS)

    # Parse events
    output = []
    for user in users:
        keyval = dict()
        keyval["login"] = user
        keyval["events"] = dict()
        keyval["events"].update({"TotalEvent":0})
        for event in events:
            if user == event["actor"]["login"]:
                keyval["events"]["TotalEvent"] += 1
                if not event["type"] in keyval["events"]:
                    keyval["events"].update({event["type"]:0})
                keyval["events"][event["type"]] += 1

        # Sort by the number of events        
        events_list = sorted(keyval["events"].items(), key=lambda t:t[1], reverse=True)
        keyval["events"] = {}
        for k, v in events_list:
            keyval["events"].update({k:v})
        

        output.append(keyval)
    
    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
    