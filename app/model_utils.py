import os
import random
import joblib, pandas as pd
from app.config import MODEL_PATH, PRED_PROB_THRESHOLD, FEATURE_COLUMNS, DEBUG_MALICIOUS_RATE
_model = None

def load_model():
    global _model
    if _model is None and os.path.exists(MODEL_PATH):
        _model = joblib.load(MODEL_PATH)
    return _model

def predict(features: dict) -> dict:
    try:
        model = load_model()
        if model is None:
            return {'label': 0, 'prob': None}
       
        ordered = {col: features.get(col, 0) for col in FEATURE_COLUMNS}
        df = pd.DataFrame([ordered])
        prob = float(model.predict_proba(df)[0,1]) if hasattr(model, 'predict_proba') else None
        label = int(model.predict(df)[0])
        if prob is not None and prob >= PRED_PROB_THRESHOLD:
            label = 1
      
        if DEBUG_MALICIOUS_RATE > 0.0 and random.random() < DEBUG_MALICIOUS_RATE:
            label = 1
        return {'label': label, 'prob': prob}
    except Exception:
        return {'label': 0, 'prob': None}
