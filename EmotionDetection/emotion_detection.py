"""
This module connects to the Watson NLP Emotion Detection service
to analyze textual input and return emotional scores.
"""
import requests
import json

def emotion_detector(text_to_analyse):
    """
    Sends text to the Watson NLP API and returns the raw JSON string response.
    """
    # Watson NLP Emotion Predict API Endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required by the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # JSON payload structure
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send the POST request
    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    
    # Return the raw text payload from the API response
    return response.text
