"""The module performs audio diarization"""

import pyannote.audio as pyaudio

class Diarizer:
    """
    Performs diarization on audio using pyannote.audio.

    Methods:
        diarize(audio_path): Performs diarization on the given audio file.
    """

    def diarize(self, audio_path):
        """
        Perform diarization on the given audio file.

        Args:
            audio_path (str): Path to the audio file for diarization.

        Returns:
            pyannote.audio.pipeline.Pipeline: Diarization results.
        """
        pipeline = pyaudio.ApplicationDiarization(
            uri=audio_path,
            sad="smn",
            pipeline=["pyAudioSMN", "pyAudioClustering"]
            )
        diarization = pipeline()
        return diarization
