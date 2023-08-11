"""Module for testing the complete integration flow."""

import unittest
from unittest.mock import Mock
from domain.transcription.transcription import Transcriber
from domain.diarization.diarization import Diarizer
from domain.sentiment_analysis.sentiment_analysis import SentimentAnalyzer
from domain.google_sheets.google_sheets import GoogleSheetsExporter

def integration_flow(transcriber, diarizer, sentiment_analyzer,
                     sheets_exporter, audio_path):
    """
    Simulates the complete integration flow:
    - Transcribe audio
    - Diarize transcript
    - Analyze sentiment
    - Prepare data
    - Export data to Google Sheets

    Args:
        transcriber (Transcriber): The Transcriber instance.
        diarizer (Diarizer): The Diarizer instance.
        sentiment_analyzer (SentimentAnalyzer): The SentimentAnalyzer instance.
        sheets_exporter (GoogleSheetsExporter): The GoogleSheetsExporter instance.
        audio_path (str): Path to the audio file.

    Returns:
        None
    """
    transcripts = transcriber.transcribe(audio_path)
    diarization = diarizer.diarize(audio_path)
    sentiment_scores = sentiment_analyzer.analyze_sentiment(transcripts)

    data = []
    for idx, (result, speaker) in enumerate(zip(transcripts, diarization)):
        data.append([idx + 1, speaker, result, sentiment_scores[idx]])

    sheets_exporter.export_to_sheets(data)

class TestIntegration(unittest.TestCase):
    """
    A test case class for testing the complete integration flow.

    Inherits:
        unittest.TestCase: The base class for all test cases in unittest.

    Attributes:
        None

    Methods:
        test_complete_flow(self): Test the complete integration flow.
    """

    def test_complete_flow(self):
        """
        Test the complete integration flow.

        This test method simulates the complete flow of transcribing an audio file,
        diarizing the transcript, analyzing sentiment, and exporting data to Google
        Sheets. It uses mocked instances of the domain classes for testing.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        # Mock domain classes for testing
        mock_transcriber = Mock(spec=Transcriber)
        mock_diarizer = Mock(spec=Diarizer)
        mock_sentiment_analyzer = Mock(spec=SentimentAnalyzer)
        mock_google_sheets_exporter = Mock(spec=GoogleSheetsExporter)

        # Set up expected results for each step

        expected_transcripts = ["Hello, how are you?", "I'm doing well, thank you."]
        expected_diarization = ["Speaker A", "Speaker B"]
        expected_sentiment_scor = [0.8, 0.6]

        # Configure mock methods to return expected results
        mock_transcriber.transcribe.return_value = expected_transcripts
        mock_diarizer.diarize.return_value = expected_diarization
        mock_sentiment_analyzer.analyze_sentiment.return_value = expected_sentiment_scor


        audio_path = "data/raw/audio.mp3"
        integration_flow(mock_transcriber,
                         mock_diarizer,
                         mock_sentiment_analyzer,
                         mock_google_sheets_exporter,
                         audio_path
                         )

        # TODO: Add assertions to validate the complete flow based on expected results

if __name__ == "__main__":
    unittest.main()
