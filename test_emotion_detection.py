from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Define the statements and their expected dominant emotions
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]

        # Iterate through each statement and check if the detected dominant emotion matches the expected one
        for statement, expected_emotion in test_cases:
            with self.subTest(statement=statement, expected_emotion=expected_emotion):
                # Call the emotion detector function with the statement
                result = emotion_detector(statement)
                
                # Assert that the dominant emotion matches the expected emotion
                self.assertEqual(result['dominant_emotion'], expected_emotion)
      
unittest.main()