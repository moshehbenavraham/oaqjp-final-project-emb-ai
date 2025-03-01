# This file is the server for the emotion detection application
from flask import Flask, render_template, request # Import the Flask framework and the request module
from EmotionDetection.emotion_detection import emotion_detector # Import the emotion_detector function from the EmotionDetection package

app = Flask(__name__) # Create a Flask application

@app.route('/') # Define the route for the home page
def index(): # Define the function for the home page
    return render_template('index.html') # Return the home page

@app.route('/emotionDetector', methods=['GET', 'POST']) # Define the route for the emotion detection page
def emotion_detector_route(): # Define the function for the emotion detection page
    if request.method == 'POST': # If the request method is POST
        text_to_analyze = request.form['text'] # Get the text input from the POST request
    else: # If the request method is GET
        text_to_analyze = request.args.get('textToAnalyze', '') # Get the text input from the GET request
    
    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)
    
    # Check if the result is valid (e.g., dominant_emotion is None or text is empty)
    if 'dominant_emotion' not in result or result['dominant_emotion'] is None or not text_to_analyze:
        return "Invalid text! Please try again!" # Return an error message
    
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