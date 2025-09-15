import os
MODEL_PATH = os.environ.get('MODEL_PATH', 'model/threat_model.joblib')
HOST = '0.0.0.0'
PORT = int(os.environ.get('PORT', 5000))
PRED_PROB_THRESHOLD = 0.5

# Features used by both training and live inference, in strict order
FEATURE_COLUMNS = [
    'pkt_len',
    'src_port',
    'dst_port',
    'protocol',
    'flags',
    'ttl',
    'entropy',
]

# Debug toggle: fraction of packets to force as malicious (0.0 disables)
DEBUG_MALICIOUS_RATE = float(os.environ.get('DEBUG_MALICIOUS_RATE', '0.0'))
