from flask import Flask, request, render_template
import pickle
import numpy as np
import time
import os

app = Flask(__name__)

weather_classes = [
    "clear",
    "cloudy",
    "drizzly",
    "foggy",
    "hazey",
    "misty",
    "rainy",
    "smokey",
    "thunderstorm",
]


def load_model(model_path="model/model.pkl"):
    """Load the trained model from disk."""
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model


def classify_weather(features):
    """Run inference and return label + latency in ms."""
    model = load_model()
    start = time.time()
    prediction_index = model.predict(features)[0]
    latency = round((time.time() - start) * 1000, 2)
    prediction = weather_classes[int(prediction_index)]
    return prediction, latency


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        # Show input form
        return render_template("form.html")

    # POST: read form values and classify
    try:
        temperature = float(request.form["temperature"])
        pressure = float(request.form["pressure"])
    except (KeyError, ValueError):
        return "Invalid input", 400

    features = np.array([[temperature, pressure]])
    prediction, latency = classify_weather(features)

    return render_template(
        "result.html",
        prediction=prediction,
        latency=latency,
        temperature=temperature,
        pressure=pressure,
    )


if __name__ == "__main__":
    # IMPORTANT: run Flask so the container keeps running
    app.run(host="0.0.0.0", port=5000)

