# loanapp/utils.py
import joblib
import os

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "ml_model", "loan_model.pkl")
    return joblib.load(model_path)
