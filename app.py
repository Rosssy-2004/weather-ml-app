from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Weather ML App</h1><p>Deployed via CI/CD pipeline.By the great group 11 !</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
