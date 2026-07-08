"""
Executing this file initiates the Flask web application deployment 
providing the backend API for emotion analysis.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Processes requests sent to the backend endpoint. Analyzes the text parameter
    and returns a formatted descriptive string of emotion scores.
    """
    # Retrieve text from the query string parameters
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Run the model logic
    response = emotion_detector(text_to_analyze)
    
    # Extract structural elements
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
        
    # Return formatted text statement to render in the UI
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the baseline HTML landing page for the application UI.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
