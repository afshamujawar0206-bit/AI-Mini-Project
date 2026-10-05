from flask import Flask, render_template, request
from model import predict_risk

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    location = request.form["location"]

    rainfall = float(request.form["rainfall"])
    water_level = float(request.form["water_level"])
    wind_speed = float(request.form["wind_speed"])

    # AI Prediction
    prediction = predict_risk(
        rainfall,
        water_level,
        wind_speed
    )

    # Warning message
    if prediction == "High":

        message = "Possible disaster risk detected. Take safety precautions immediately."

        warning = "Next 30 minutes may be critical."

    elif prediction == "Medium":

        message = "Stay alert and monitor the situation."

        warning = "Keep emergency items ready."

    else:

        message = "No immediate high risk detected."

        warning = "Continue normal monitoring."

    return render_template(
        "index.html",
        location=location,
        rainfall=rainfall,
        water_level=water_level,
        wind_speed=wind_speed,
        prediction=prediction,
        message=message,
        warning=warning
    )


if __name__ == "__main__":
    app.run(debug=True)