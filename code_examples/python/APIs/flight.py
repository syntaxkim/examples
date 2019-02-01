import requests

def main():
    flight_id = int(input("flight_id: "))
    # It only works when /project1/application5.py is running.
    res = requests.get(f"http://127.0.0.1:5000/api/flights/{flight_id}")
    data = res.text
    print(data)

if __name__ == "__main__":
    main()

''' (server-side source)
# Building out your own API.
@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    """Return details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        # jsonify function (from flask) takes a Python dictionary, converts it into a JSON object
        # and puts all required HTTP headers on it.
        return jsonify({"error": "Invalid flight_id"}), 422
        # When Flask returns something, status code 200 is returned by default.
        # To see the response with a status code 422, go with a non-existent flight_id

    # Get all passengers.
    passengers = flight.passengers
    names = []
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({
        "origin": flight.origin,
        "destination": flight.destination,
        "duration": flight.duration,
        "passengers": names
    })
    # To not have the keys sorted alphabetically, albeit not recommended, 
    # add 'app.config['JSON_SORT_KEYS'] = False'
    # Refer to https://stackoverflow.com/questions/43263356/prevent-flask-jsonify-from-sorting-the-data
'''