from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form.get("name")
        if not name:
            return "Who are you?"
        else:
            return f"Hello, {name}"

if __name__ == "__main__":
    app.run()