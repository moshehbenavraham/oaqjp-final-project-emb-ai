# emotion_detection.py
# Import necessary libraries
import requests # Import the requests library for making HTTP requests
import json # Import the json library for parsing JSON data

# Define the emotion_detector function
def emotion_detector(text_to_analyze):
    # Define the URL and headers for the Watson NLP API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the model ID for the emotion prediction
    
    # Define the input JSON for the API request
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send the request to the Watson NLP API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Convert response text to dictionary
    response_dict = json.loads(response.text)
    
    # Extract emotion scores from the first emotion prediction
    emotions = response_dict['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger'] # Extract the anger score
    disgust_score = emotions['disgust'] # Extract the disgust score
    fear_score = emotions['fear'] # Extract the fear score
    joy_score = emotions['joy'] # Extract the joy score
    sadness_score = emotions['sadness'] # Extract the sadness score
    
    # Find the dominant emotion
    emotion_scores = {
        'anger': anger_score, # Set the anger score
        'disgust': disgust_score, # Set the disgust score
        'fear': fear_score, # Set the fear score
        'joy': joy_score, # Set the joy score
        'sadness': sadness_score # Set the sadness score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get) # Find the dominant emotion
    
    # Return the formatted dictionary
    return {
        'anger': anger_score, # Set the anger score
        'disgust': disgust_score, # Set the disgust score
        'fear': fear_score, # Set the fear score
        'joy': joy_score, # Set the joy score
        'sadness': sadness_score, # Set the sadness score
        'dominant_emotion': dominant_emotion # Set the dominant emotion
    }

# Test the emotion_detector function
print(emotion_detector("I am so happy I am doing this."))

# Test the emotion_detector function
print(emotion_detector("I am so sad I am doing this."))

# Test the emotion_detector function
print(emotion_detector("I am so angry I am doing this."))

# Test the emotion_detector function
print(emotion_detector("I am so disgusted I am doing this."))

# Test the emotion_detector function
print(emotion_detector("I am so fearful I am doing this."))
