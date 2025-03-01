import unittest # Import the unittest framework
from EmotionDetection.emotion_detection import emotion_detector # Import the emotion_detector function from the EmotionDetection package

class TestEmotionDetection(unittest.TestCase): # Define a class for the unit tests
    
    def test_joy_dominant(self): # Define a test method for the joy dominant emotion
        statement = "I am glad this happened" # Define the statement to test
        result = emotion_detector(statement) # Call the emotion_detector function with the statement
        expected = 'joy' # Define the expected result
        self.assertEqual(result['dominant_emotion'], expected, 
                        msg=f"Expected dominant emotion '{expected}' for '{statement}', got {result}") # Assert that the result is equal to the expected result
        print(f"Test Joy: '{statement}' -> {result}") # Print the result
    
    def test_anger_dominant(self):
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        expected = 'anger'
        self.assertEqual(result['dominant_emotion'], expected,
                        msg=f"Expected dominant emotion '{expected}' for '{statement}', got {result}")
        print(f"Test Anger: '{statement}' -> {result}")
    
    def test_disgust_dominant(self):
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        expected = 'disgust'
        self.assertEqual(result['dominant_emotion'], expected,
                        msg=f"Expected dominant emotion '{expected}' for '{statement}', got {result}")
        print(f"Test Disgust: '{statement}' -> {result}")
    
    def test_sadness_dominant(self):
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        expected = 'sadness'
        self.assertEqual(result['dominant_emotion'], expected,
                        msg=f"Expected dominant emotion '{expected}' for '{statement}', got {result}")
        print(f"Test Sadness: '{statement}' -> {result}")
    
    def test_fear_dominant(self):
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        expected = 'fear'
        self.assertEqual(result['dominant_emotion'], expected,
                        msg=f"Expected dominant emotion '{expected}' for '{statement}', got {result}")
        print(f"Test Fear: '{statement}' -> {result}")

# If the script is run directly, execute the unit tests
if __name__ == '__main__':
    unittest.main(verbosity=2) # Execute the unit tests

