from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import threading, time, os
from app.packet_capture import start_sniff, packet_queue
from app.model_utils import load_model, predict
from app.config import HOST, PORT

app = Flask(__name__, template_folder='templates', static_folder='static')
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify({'status': 'ok'})

def prediction_loop():
    while True:
        try:
            item = packet_queue.get()
            feats = item.get('features', {})
            ts = item.get('ts', time.time())
            res = predict(feats)
            payload = {'features': feats, 'result': res, 'ts': ts}
            socketio.emit('packet_prediction', payload)
        except Exception:
            pass
        finally:
            time.sleep(0.01)

if __name__ == '__main__':
    try:
        load_model()
    except Exception as e:
        print('Model not loaded yet:', e)
    start_sniff(interface=None)
    t = threading.Thread(target=prediction_loop, daemon=True)
    t.start()
    socketio.run(app, host=HOST, port=PORT)
