"""Module for testing the functionality of the Diarizer class."""

import unittest
from domain.diarization.diarization import Diarizer

class DiarizationService:
    """
    A service class that abstracts the diarization functionality.

    This class provides a high-level interface for performing diarization
    on an audio file using the Diarizer class.

    Attributes:
        None

    Methods:
        diarize(self, audio_file): Diarize an audio file using the Diarizer class.

    """
    def diarize(self, audio_file):
        """
        Diarizes an audio file using the Diarizer class.

        Args:
            audio_file (str): The path to the audio file for diarization.

        Returns:
            dict: The diarization result containing speaker segments.

        """
        return Diarizer().diarize(audio_file)

class TestDiarization(unittest.TestCase):
    """
    A test case class for testing the functionality of diarization.

    Inherits:
        unittest.TestCase: The base class for all test cases in unittest.

    Attributes:
        None

    Methods:
        setUp(self): Set up the test case by initializing
                     the `DiarizationService` instance.
        test_diarize_audio(self): Test the `diarize` method of
                                  the DiarizationService class.

    """

    def setUp(self):
        """
        Initializes the test case by setting up the `DiarizationService` instance.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        self.diarization_service = DiarizationService()

    def test_diarize_audio(self):
        """
        Test the `diarize` method of the DiarizationService class
        by diarizing an audio file.

        This test method performs the diarization process on an audio file and
        then makes specific assertions to validate the diarization result.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        result = self.diarization_service.diarize("data/raw/audio.mp3")

        # Validate the diarization result
        self._assert_diarization_result(result)

    def _assert_diarization_result(self, result):
        """
        Perform assertions to validate the diarization result.

        Args:
            result (dict): The diarization result to be validated.

        Returns:
            None
        """
        self.assertIsInstance(result, dict)
        self.assertIn("speakers", result)
        self.assertIsInstance(result["speakers"], list)
        self.assertGreater(len(result["speakers"]), 0)

        # TODO: Add more specific assertions based on the expected output

if __name__ == "__main__":
    unittest.main()
