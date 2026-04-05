# ⚡ Global EV Charging Behaviour — Prediction & Analysis

> A Machine Learning web application that predicts the success of Electric Vehicle charging sessions using real-world behavioural features like battery capacity, session duration, energy delivered, and ambient temperature.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Model Details](#model-details)
- [Prerequisites & Installation](#prerequisites--installation)
- [How to Run](#how-to-run)
- [API Reference](#api-reference)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## 🌍 Overview

The **Global EV Charging Behaviour** project studies and predicts patterns in Electric Vehicle (EV) charging sessions across diverse geographies and use cases. With EV adoption accelerating worldwide, understanding *when*, *how*, and *how successfully* vehicles charge is critical for infrastructure planning and grid management.

This project provides:
- A **trained ML pipeline** to predict whether a charging session will succeed or fail.
- A **Flask-powered web application** with a clean user interface for real-time predictions.
- An **exploratory data analysis (EDA)** notebook for insights into global charging behaviour trends.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🤖 **Gradient Boosting Classifier** | High-accuracy model trained on engineered EV session features |
| 🔧 **Smart Preprocessing** | Automated feature engineering — temperature binning, duration categorisation, and more |
| 🌐 **Flask Web App** | Lightweight backend with a responsive Bootstrap-powered frontend |
| ⚡ **Real-time Prediction** | Instant `Success` / `Failed` output for any new charging session input |
| 📊 **EDA Notebook** | Deep-dive analysis of global charging behaviour patterns |
| 🗂️ **Mock Data Generator** | Script to generate synthetic datasets for testing and development |

---

## 📂 Project Structure

```text
Global-EV-Charging/
│
├── templates/
│   └── index.html                  # Frontend web interface (HTML + Bootstrap)
│
├── app.py                          # Flask backend — routing & prediction logic
├── ev.py                           # Standalone preprocessing & model training script
├── ev.ipynb                        # Jupyter Notebook — EDA, preprocessing & training
├── generate_data.py                # Script to generate synthetic/mock EV session data
│
├── gradient_boosting_model.pkl     # Serialised trained Gradient Boosting model
├── preprocessor.pkl                # Serialised preprocessing pipeline (encoders + scalers)
│
├── requirements.txt                # All Python dependencies
└── README.md                       # Project documentation (this file)
```

---

## 📊 Dataset

The dataset (real or synthetically generated via `generate_data.py`) consists of EV charging session records with the following key features:

| Column | Description |
|---|---|
| `battery_capacity_kwh` | Total battery capacity of the EV (in kWh) |
| `session_duration_min` | Duration of the charging session (in minutes) |
| `energy_delivered_kwh` | Actual energy delivered during the session (in kWh) |
| `start_time_hour` | Hour of the day the session started (0–23) |
| `temperature_c` | Ambient temperature during charging (in °C) |
| `charger_type` | Type of charger used (AC Level 1 / AC Level 2 / DC Fast) |
| `location_type` | Location category (Home / Public / Workplace) |
| `charging_status` | **Target variable** — `Success` or `Failed` |

> 📌 The synthetic dataset can be regenerated at any time using `python generate_data.py`.

---

## 🧠 Model Details

The prediction pipeline consists of two serialised components:

### 1. `preprocessor.pkl` — Preprocessing Pipeline
- **Numerical features:** StandardScaler normalisation
- **Categorical features:** OneHotEncoder (handles unseen categories gracefully)
- **Engineered features:**
  - `temp_category` — bins temperature into `Cold`, `Moderate`, `Hot`
  - `duration_bound` — categorises session duration as `Short`, `Medium`, `Long`
  - `energy_efficiency` — ratio of energy delivered to battery capacity

### 2. `gradient_boosting_model.pkl` — Classifier
- **Algorithm:** Gradient Boosting Classifier (`sklearn.ensemble.GradientBoostingClassifier`)
- **Tuned hyperparameters:** `n_estimators`, `learning_rate`, `max_depth`
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score, ROC-AUC
- **Output Classes:** `Success` (1) / `Failed` (0)

---

## ⚙️ Prerequisites & Installation

### Requirements
- Python **3.8+**
- pip package manager

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/global-ev-charging.git
   cd global-ev-charging
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   venv\Scripts\activate           # On Windows
   ```

3. **Install all dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Key packages used:
   ```
   flask
   pandas
   numpy
   scikit-learn
   joblib
   ```

4. **(Optional) Regenerate the dataset:**
   ```bash
   python generate_data.py
   ```

5. **(Optional) Retrain the model:**
   ```bash
   python ev.py
   ```

---

## 💡 How to Run

1. **Start the Flask development server:**
   ```bash
   python app.py
   ```

2. **You should see output similar to:**
   ```
    * Running on http://127.0.0.1:5000
    * Debug mode: on
   ```

3. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

4. **Fill in the prediction form** with values like:
   - Battery Capacity (kWh)
   - Session Duration (minutes)
   - Energy Delivered (kWh)
   - Start Time (hour)
   - Temperature (°C)
   - Charger Type & Location

5. **Click `Predict Status`** — the result (`✅ Success` or `❌ Failed`) will appear instantly.

---

## 🔌 API Reference

The Flask app exposes a simple prediction endpoint:

### `POST /predict`

**Request Body (JSON):**
```json
{
  "battery_capacity_kwh": 60,
  "session_duration_min": 45,
  "energy_delivered_kwh": 30,
  "start_time_hour": 9,
  "temperature_c": 22,
  "charger_type": "AC Level 2",
  "location_type": "Public"
}
```

**Response:**
```json
{
  "prediction": "Success",
  "confidence": 0.87
}
```

---

## 🔮 Future Improvements

- [ ] Add support for multi-country geolocation data to capture regional behaviour differences
- [ ] Integrate live weather API for automatic temperature input
- [ ] Expand model to predict **charging duration** (regression task)
- [ ] Deploy to cloud (AWS / GCP / Render) with a public URL
- [ ] Add time-series analysis for peak charging demand forecasting
- [ ] Interactive dashboard using Plotly / Streamlit for EDA visualisation

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add: your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please ensure your code follows PEP 8 style guidelines and includes appropriate comments.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Made with ❤️ for a greener, smarter EV future 🌱
</div>
