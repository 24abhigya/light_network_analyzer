Lightweight AI-Powered Network Packet Analyzer


Contents:
- app/: Flask app and static frontend
- train/: sample dataset and training script

Run instructions:
1. Create virtualenv and install deps:
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
2. Train model:
   python train/train_model.py --csv train/sample_dataset.csv --out model/threat_model.joblib
3. Run app (may need sudo for sniffing):
   sudo python app/app.py
Open http://localhost:5000
