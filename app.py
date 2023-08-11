"""The app for analyzing Call Quality Rate (CQR)
of call transcripts based on audio recordings.
"""

import streamlit as st
from domain.transcription.transcription import Transcriber
from domain.diarization.diarization import Diarizer
from domain.sentiment_analysis.sentiment_analysis import SentimentAnalyzer
from domain.google_sheets.google_sheets import GoogleSheetsExporter

class CallQualityRateApp:
    """
    CallQualityRateApp class manages the Streamlit web app for analyzing
    Call Quality Rate (CQR) of call transcripts based on audio recordings.

    Attributes:
        transcriber (Transcriber): An instance of the Transcriber class
                                   for audio transcription.
        diarizer (Diarizer): An instance of the Diarizer class for diarization.
        sentiment_analyzer (SentimentAnalyzer): An instance of the SentimentAnalyzer
                                                class for sentiment analysis.
        google_sheets_exporter (GoogleSheetsExporter): An instance of
                                the GoogleSheetsExporter class for exporting results.

    Methods:
        analyze_transcript(uploaded_file): Analyzes the uploaded audio file to calculate
                                           CQR and export results.
        run(): Runs the Streamlit web app, allowing users to upload and analyze
               audio files.
    """

    def __init__(self):
        self.transcriber = Transcriber(model_path="models/vosk-model-ru-0.42.zip")
        self.diarizer = Diarizer()
        self.sentiment_analyzer = SentimentAnalyzer(model_name="paraphrase-multilingual-MiniLM-L12-v2")
        self.google_sheets_exporter = GoogleSheetsExporter(credentials_path="credentials.json")

    def analyze_transcript(self, uploaded_file):
        """
        Analyzes the uploaded audio file to calculate Call Quality Rate (CQR)
        and export results to Google Sheets.

        Args:
            uploaded_file (FileUploader): The uploaded audio file.

        Returns:
            None
        """
        transcript = self.transcriber.transcribe(uploaded_file)
        diarization_result = self.diarizer.diarize(uploaded_file)

        sentences = [item["text"] for item in transcript]
        sentiment_scores = self.sentiment_analyzer.analyze_sentiment(sentences)

        st.write("Sentiment Scores:")
        for i, score in enumerate(sentiment_scores):
            st.write(f"Sentence {i + 1}: {score:.4f}")

        cqr_score = sum(sentiment_scores)
        st.write(f"Call Quality Rate (CQR): {cqr_score:.4f}")

        if st.button("Export Results to Google Sheets"):
            data_to_export = [["Transcript", "Speaker", "Sentiment Score"]]
            for item in transcript:
                speaker = diarization_result[item["start"]].pop("speaker")
                sentiment_score = sentiment_scores.pop(0)
                data_to_export.append([item["text"], speaker, sentiment_score])
            self.google_sheets_exporter.export_to_sheets(data_to_export)
            st.success("Results exported to Google Sheets!")

    def run(self):
        """
        Runs the Streamlit web app, allowing users to upload and analyze audio files.

        Returns:
            None
        """
        st.title("Call Quality Rate Web App")
        st.write("Upload an audio file to analyze Call Quality Rate (CQR) of call transcripts.")

        uploaded_file = st.file_uploader("Upload an audio file (WAV or MP3 format)", type=["wav", "mp3"])

        if uploaded_file:
            self.analyze_transcript(uploaded_file)

        st.write("Author: Denis Chunarev")
        st.write("Last Updated: 2023-08-11")

if __name__ == "__main__":
    app = CallQualityRateApp()
    app.run()
