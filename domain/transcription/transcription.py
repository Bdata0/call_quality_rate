"""This module transcribes audio files into text format."""

import vosk

class Transcriber:
    """
    Transcribes audio using the Vosk model.

    Args:
        model_path (str): Path to the Vosk model directory.

    Attributes:
        model (vosk.Model): Vosk model for speech recognition.

    Methods:
        transcribe(audio_path): Transcribes the given audio file.
    """

    def __init__(self, model_path):
        """
        Initialize the Transcriber with the Vosk model.

        Args:
            model_path (str): Path to the Vosk model directory.
        """
        self.model_path = model_path

    def _extract_model(self):
        """
        Extracts the model from a zipfile.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        with zipfile.ZipFile(self.model_path, "r") as zip_ref:
            zip_ref.extractall("domain/transcription/models")

    def transcribe(self, audio_path):
        """
        Transcribe the given audio file.

        Args:
            audio_path (str): Path to the audio file for transcription.

        Yields:
            str: Transcription result for each audio chunk.
        """
        self._extract_model()
        self.model = vosk.Model("domain/transcription/models/vosk-model-ru-0.42")
        recognizer = vosk.KaldiRecognizer(self.model, 16000)
        with open(audio_path, "rb") as audio_file:
            while True:
                data = audio_file.read(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    result = recognizer.Result()
                    yield result
