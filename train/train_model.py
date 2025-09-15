import argparse
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from app.config import FEATURE_COLUMNS, MODEL_PATH

parser = argparse.ArgumentParser()
parser.add_argument('--csv', required=True)
parser.add_argument('--out', default=MODEL_PATH)
args = parser.parse_args()

df = pd.read_csv(args.csv)

# Ensure required columns exist
required_cols = FEATURE_COLUMNS + ['label']
missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns in CSV: {missing}. CSV must include {required_cols}")

X = df[FEATURE_COLUMNS]
y = df['label']

clf = RandomForestClassifier(n_estimators=200, max_depth=None, random_state=42, n_jobs=-1)
clf.fit(X, y)

os.makedirs(os.path.dirname(args.out), exist_ok=True)
joblib.dump(clf, args.out)
print('Model saved to', args.out)
