from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk



def find_text_emotion(txt, sentiment):
    """find and returns the emotion of the text in a given doc field"""
    try:
        compound = sentiment.polarity_scores(txt).get('compound', 0)
        # Return the emotion based on the compound score
        if compound <= -0.5:
            return 'negative'
        elif -0.50 < compound < 0.5:
            return 'neutral'
        elif compound >= 0.5:
            return 'positive'

    except Exception as e:
        raise Exception(f"An error occurred while finding text emotion: {e}")

