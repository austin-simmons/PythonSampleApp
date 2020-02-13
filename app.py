from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>It Works!</h1>"


@app.route("/hello/<name>")
def get_name(name):
    return f"<h1>Hello {name}!</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
