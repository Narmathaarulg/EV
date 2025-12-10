EV Charging Success Prediction – Project Documentation
1. Project Title

Electric Vehicle (EV) Charging Success Prediction using Machine Learning

2. Objective

The project aims to predict the success of EV charging sessions to help optimize charging performance and reduce downtime. This allows better planning for EV owners and charging station operators.

3. Problem Statement

Efficient EV charging is critical as the number of electric vehicles increases. Charging sessions can fail due to multiple factors such as battery health, station availability, or charging time. Predicting the success of a charging session can improve user experience and operational efficiency.

4. Data Collection

The data was sourced from publicly available EV charging datasets on Kaggle.

Dataset includes features such as:

Battery level

Charging duration

Time of day

Station location

Vehicle type

Target variable: Success (Yes/No)

5. Data Preprocessing

Handled missing values

Standardized numerical features

Encoded categorical variables

Split data into training and testing sets

6. Model Selection

Several models were evaluated:

Linear Regression

Logistic Regression

Support Vector Machine (SVM)

Gradient Boosting

Gradient Boosting was selected as it gave the best performance (highest R² score).

7. Implementation

Jupyter Notebook:

Data exploration

Preprocessing

Model training and evaluation

Saved Models:

gradient_boosting_model.pkl – Trained model

ev_charging3_preprocessor.pkl – Preprocessing pipeline

ev_charging3_success_predictor.pkl – Helper functions for prediction

Flask Web App:

Allows users to input charging session details

Displays predicted outcome

Easy-to-use front-end interface

8. Repository Structure
EV/
├── notebooks/          # Jupyter notebooks
├── models/             # Saved machine learning models
├── scripts/            # Python scripts for prediction
├── requirements.txt    # Project dependencies
├── .gitignore          # Ignored files/folders
└── README.md           # GitHub readme

9. Installation

Clone the repository:

git clone https://github.com/Narmathaarulg/EV.git
cd EV


Create a virtual environment:

python -m venv .venv
.\.venv\Scripts\activate   # Windows


Install dependencies:

pip install -r requirements.txt

10. Usage

Run the Flask application:

python scripts/ev.py


Open a browser and go to:

http://127.0.0.1:5000/


Enter EV session details to get predictions.

11. Results

Gradient Boosting achieved the highest accuracy and R² score.

Users can reliably predict whether a charging session will succeed.

12. Conclusion

This project demonstrates the application of machine learning to optimize EV charging operations. The system is extendable and can be integrated into charging station management platforms.

13. Future Work

Integrate real-time data from charging stations

Build a mobile application for predictions

Test additional machine learning models (e.g., XGBoost, LightGBM) for improved performance

14. References

Kaggle EV Charging Datasets

Scikit-learn Documentation

Flask Documentation
