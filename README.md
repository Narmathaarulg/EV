EV Charging Success Prediction
Project Overview

This project predicts the success of electric vehicle (EV) charging sessions using machine learning. The goal is to help optimize EV charging performance by providing accurate predictions based on historical data.

The project includes:

Data preprocessing and feature engineering

Machine learning model training (Gradient Boosting)

A Flask web application for user-friendly predictions

Repository Structure
EV/
├── notebooks/              # Jupyter notebooks
│   └── ev.ipynb            # Exploratory Data Analysis and modeling
├── models/                 # Saved model files
│   ├── gradient_boosting_model.pkl
│   ├── ev_charging3_preprocessor.pkl
│   └── ev_charging3_success_predictor.pkl
├── scripts/                # Python scripts
│   └── ev.py               # Main script for predictions
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files/folders
└── README.md               # Project documentation

Installation

Clone the repository:

git clone https://github.com/Narmathaarulg/EV.git
cd EV


Create and activate a virtual environment:

python -m venv .venv
.\.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux


Install dependencies:

pip install -r requirements.txt

Usage

Run the Flask application:

python scripts/ev.py


Open your web browser and go to:

http://127.0.0.1:5000/


Input the required features and get predictions for EV charging success.

Model Details

Algorithm Used: Gradient Boosting

Evaluation Metric: R² Score

Preprocessing: Standardization, handling missing values

Contributing

Contributions are welcome! Please create a pull request or submit issues if you find bugs or have suggestions.
