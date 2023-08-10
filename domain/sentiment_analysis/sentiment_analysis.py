"""The module performs speaker's analyzes sentiment."""

from sentence_transformers import SentenceTransformer, util

class SentimentAnalyzer:
    """
    Analyzes sentiment using the SentenceTransformer model.

    Args:
        model_name (str): Name of the SentenceTransformer model.

    Attributes:
        model (SentenceTransformer): SentenceTransformer model for sentiment analysis.

    Methods:
        analyze_sentiment(sentences): Analyzes sentiment of given sentences.
    """

    def __init__(self, model_name):
        """
        Initialize the SentimentAnalyzer with the SentenceTransformer model.

        Args:
            model_name (str): Name of the SentenceTransformer model.
        """
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name)

    def analyze_sentiment(self, sentences):
        """
        Analyze the sentiment of given sentences.

        Args:
            sentences (List[str]): List of sentences for sentiment analysis.

        Returns:
            List[float]: List of sentiment scores for each sentence.
        """
        scores = self.model.encode(sentences, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(scores, scores)
        sentiment_scores = cos_scores.sum(dim=1).tolist()
        return sentiment_scores
