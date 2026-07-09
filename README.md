# Emotion Detector Web Application

An AI-based web application developed using Python, Flask, and the IBM Watson NLP library. This application analyzes text provided by the user and detects underlying emotions, providing scores for anger, disgust, fear, joy, and sadness, along with identifying the dominant emotion.

## Features
- **Watson NLP Integration:** Communicates with the Watson NLP Emotion Detection service to process raw text data.
- **Robust Error Handling:** Seamlessly manages blank or invalid user inputs, returning clear system error alerts rather than crashing.
- **Unit Tested:** Includes a full suite of automated unit tests using the Python `unittest` library to verify prediction accuracy.
- **Strict Code Quality:** Fully compliant with PEP 8 standards, scoring 10/10 on static code analysis using `pylint`.

## Project Structure
- `EmotionDetection/`: Package containing the core logic and Watson API integration.
- `server.py`: Flask application server that manages routes and handles web interface requests.
- `test_emotion_detection.py`: Unit testing suite.
- `templates/index.html`: The web front-end interface.

## How to Run the Application

1. Clone the repository to your local environment or development IDE.
2. Ensure required dependencies are installed:
   ```bash
   pip install requests flask pylint
