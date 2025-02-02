from flask import Flask, render_template, request
import numpy as np
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("rainfall_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        pressure = float(request.form["pressure"])
        dewpoint = float(request.form["dewpoint"])
        humidity = float(request.form["humidity"])
        cloud = float(request.form["cloud"])
        sunshine = float(request.form["sunshine"])
        winddirection = float(request.form["winddirection"])
        windspeed = float(request.form["windspeed"])

        # Create an array for the model
        features = np.array([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])

        # Make prediction
        prediction = model.predict(features)[0]
        result = "Yes! High chances of rainfall 🌧️" if prediction == 1 else "No! No chances of rainfall ☀️"

        return render_template("result.html", result=result)

    except Exception as e:
        return render_template("result.html", result="Error: Invalid input!")

if __name__ == "__main__":
    app.run(debug=True)
