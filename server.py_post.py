# This file is the server for the emotion detection application
# It uses Flask to create a web application that allows users to input a text and get the dominant emotion

from flask import Flask, render_template, request # Import the Flask framework and the request module
from EmotionDetection.emotion_detection import emotion_detector # Import the emotion_detector function from the EmotionDetection package

app = Flask(__name__) # Create a Flask application

@app.route('/') # Define the route for the home page
def index(): # Define the function for the home page
    return render_template('index.html') # Return the home page

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    # Get the text input from the POST request
    text_to_analyze = request.form['text']
    
    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)
    
    # Check if the result is valid (e.g., not an error or None)
    if 'dominant_emotion' not in result:
        return "Invalid text! Please try again."
    
    # Format the response as per the customer's request
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    
    return response

# If the script is run directly, run the Flask application
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) # Run the Flask application on localhost at port 5000 with debugging enabled
