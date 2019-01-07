from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    rate=None

    if request.method == 'POST':
        data = request.get_json()

        base = data["base"].upper()
        other = data["other"].upper()

        r = requests.get('https://api.exchangeratesapi.io/latest', params={'base': base, 'symbols': other})

        if r.status_code != 200:
            raise Exception("Error: API request unsuccessful.")

        data = r.json()

        if other not in data['rates']:
            return jsonify({"success": False})

        return jsonify({
            "success": True,
            "base": base,
            "other": other,
            "rates": data["rates"][other]
            })

    return render_template('index.html', rate=rate)

if __name__ == '__main__':
    app.run()