"""Module for testing the functionality of the Transcriber class."""

import unittest
from domain.transcription.transcription import Transcriber

class TestTranscriber(unittest.TestCase):
    """
    A test case class for testing the functionality of the Transcriber class.

    Inherits:
        unittest.TestCase: The base class for all test cases in unittest.

    Attributes:
        None

    Methods:
        setUp(self): Set up the test case by initializing the `transcriber` attribute
                     with the Vosk speech recognition model for the Russian language.
        test_transcribe(self): Test the `transcribe` method of the Transcriber class.
        tearDown(self): Clean up after the test case by deleting the `transcriber`
                        attribute.

    """

    def setUp(self):
        """
        Set up the test case by initializing the `transcribe` attribute
        with the Vosk speech recognition model for the Russian language.

        Parameters:
            self (TestClass): The instance of the test class.

        Returns:
            None
        """
        self.transcriber = Transcriber("models/vosk-model-ru-0.42")

    def test_transcribe_audio(self):
        """
        Test the transcribe_audio function.

        This function tests the functionality of the transcribe_audio method
        in the current class. It calls the transcribe_audio method with a
        specified audio file path and checks the type and content of the returned result

        Returns:
            None
        """
        result = self.transcriber.transcribe("data/raw/audio.mp3")
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, str) for item in result))

if __name__ == "__main__":
    unittest.main()
