

def main():
    events = {"total": 10, "foo": 1, "bar": 2, "bazz": 100}

    haha = dict()
    
    events_list = sorted(events.items(), key=lambda t:t[1], reverse=True)

    print(events_list)

    for k, v in events_list:
        haha.update({k:v})

    print(events)

    print(haha)
    
    

if __name__ == "__main__":
    main()