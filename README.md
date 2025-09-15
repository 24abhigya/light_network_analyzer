# Light Network Analyzer

A lightweight AI-powered network packet analyzer that provides real-time threat detection and network monitoring capabilities.

## Features

- 🔍 **Real-time Packet Capture**: Monitors network traffic in real-time
- 🤖 **AI-Powered Analysis**: Uses machine learning to detect potential threats
- 📊 **Interactive Dashboard**: Web-based interface for monitoring and analysis
- 🚨 **Threat Detection**: Identifies suspicious network patterns
- 📈 **Live Updates**: Real-time updates via WebSocket connections

## Project Structure

```
light_network_analyzer/
├── app/                    # Flask application
│   ├── app.py             # Main Flask app
│   ├── config.py          # Configuration settings
│   ├── model_utils.py     # ML model utilities
│   ├── packet_capture.py  # Packet capture functionality
│   ├── static/            # Static web assets
│   │   ├── css/
│   │   └── js/
│   └── templates/         # HTML templates
├── train/                 # Training scripts and data
│   ├── sample_dataset.csv # Sample training data
│   └── train_model.py     # Model training script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Administrator/root privileges (for packet capture)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/24abhigya/light_network_analyzer.git
   cd light_network_analyzer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model**
   ```bash
   python train/train_model.py --csv train/sample_dataset.csv --out model/threat_model.joblib
   ```

5. **Run the application**
   ```bash
   # On Windows (run as Administrator):
   python app/app.py
   
   # On Linux/Mac (may need sudo):
   sudo python app/app.py
   ```

6. **Access the web interface**
   Open your browser and navigate to: `http://localhost:5000`

## Usage

1. **Start the application** following the installation steps above
2. **Open the web interface** at `http://localhost:5000`
3. **Monitor network traffic** in real-time through the dashboard
4. **View threat detections** as they are identified by the AI model

## Configuration

The application can be configured through `app/config.py`:
- Host and port settings
- Model parameters
- Capture interface settings

## Dependencies

- **Flask**: Web framework
- **Flask-SocketIO**: Real-time communication
- **Scapy**: Packet capture and analysis
- **Scikit-learn**: Machine learning
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Abhigya Srivastava** - [@24abhigya](https://github.com/24abhigya)

## Acknowledgments

- Built with Flask and modern web technologies
- Uses Scapy for network packet analysis
- Machine learning powered by scikit-learn
