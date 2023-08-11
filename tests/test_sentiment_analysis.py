"""Module for testing the functionality of the SentimentAnalyzer class."""

import unittest
from domain.sentiment_analysis.sentiment_analysis import SentimentAnalyzer

class SentimentAnalysisService:
    """
    A service class that abstracts the sentiment analysis functionality.

    This class provides a high-level interface for analyzing sentiment
    of text using the SentimentAnalyzer class.

    Attributes:
        None

    Methods:
        analyze_sentiment(self, sentences): Analyze sentiment of a list of sentences.

    """
    def __init__(self, model_name):
        self.analyzer = SentimentAnalyzer(model_name)

    def analyze_sentiment(self, sentences):
        """
        Analyzes sentiment of a list of sentences using the SentimentAnalyzer class.

        Args:
            sentences (List[str]): List of sentences to analyze.

        Returns:
            List[float]: List of sentiment scores corresponding to the input sentences.

        """
        return self.analyzer.analyze_sentiment(sentences)

class TestSentimentAnalyzer(unittest.TestCase):
    """
    A test case class for testing the functionality of sentiment analysis.

    Inherits:
        unittest.TestCase: The base class for all test cases in unittest.

    Attributes:
        None

    Methods:
        setUp(self): Set up the test case by initializing
                     the `SentimentAnalysisService` instance.
        test_analyze_sentiment(self): Test the `analyze_sentiment` method
                                      of the SentimentAnalysisService class.

    """

    def setUp(self):
        """
        Initializes the test case by setting up the `SentimentAnalysisService` instance.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        self.sentiment_service = SentimentAnalysisService(
            "paraphrase-multilingual-MiniLM-L12-v2"
            )

    def test_analyze_sentiment(self):
        """
        Test the `analyze_sentiment` method of the SentimentAnalysisService class.

        This test method analyzes the sentiment of a list of sentences
        and then makes specific assertions to validate the sentiment scores.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        sentences = ["I am happy.", "I am sad."]
        scores = self.sentiment_service.analyze_sentiment(sentences)

        # Validate the sentiment scores
        self.assertIsInstance(scores, list)
        self.assertEqual(len(scores), len(sentences))
        for score in scores:
            self.assertIsInstance(score, float)

if __name__ == "__main__":
    unittest.main()
