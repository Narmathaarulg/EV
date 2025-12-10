from flask import Flask, request, render_template
import joblib
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load ML pipeline
try:
    pipeline = joblib.load("gradient_boosting_model.pkl")
    print("Model loaded successfully")
except Exception as e:
    print("Model load failed:", e)
    pipeline = None


@app.route("/")
def home():
    return render_template("index.html", current_year=datetime.now().year)


@app.route("/predict", methods=["POST"])
def predict():
    if pipeline is None:
        return render_template("index.html", error="Model not loaded")

    try:
        # User form inputs
        input_data = {
            "Battery Capacity (kWh)": float(request.form["battery_capacity"]),
            "Charging Duration (mins)": float(request.form["duration"]),
            "Energy Delivered (kWh)": float(request.form["energy"]),
            "Charging Cost ($)": float(request.form["cost"]),
            "Temperature (°C)": float(request.form["temperature"]),
            "Station Utilization Rate (%)": float(request.form["utilization"]),
            "Charging Hour": int(request.form["hour"]),
            "Charging Day": int(request.form["day"]),
            "Charging Month": int(request.form["month"]),
            "Charging Day of Week": int(request.form["day_of_week"]),
            "Charging Speed (kWh per min)": float(request.form["speed"]),
            "Cost per kWh": float(request.form["cost_per_kwh"]),
            "Battery Percentage Charged": float(request.form["percentage_charged"]),
            "Country": request.form["country"],
            "City": request.form["city"],
            "Charging Station Type": request.form["station_type"],
            "Manufacturer": request.form["manufacturer"],
            "Payment Method": request.form["payment"],
            "Temperature Category": request.form["temp_cat"],
            "Duration Category": request.form["duration_cat"]
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # Predict using pipeline
        prediction = pipeline.predict(input_df)[0]

        msg = (
            "✅ Charging Will Likely Complete"
            if prediction == 1
            else "❌ Charging May Not Complete"
        )

        return render_template("index.html", result={"prediction": msg})

    except Exception as e:
        return render_template("index.html", error=f"Prediction failed: {e}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
