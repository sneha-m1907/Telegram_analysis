import pandas as pd 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the cleaned data
df = pd.read_csv('cleaned_messages.csv')
print(f"Number of NaN values in 'cleaned_message': {df['cleaned_message'].isna().sum()}")

# Handle NaN values by replacing them with an empty string
df['cleaned_message'] = df['cleaned_message'].fillna('')

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)
    return score['compound']  # Returns a sentiment score between -1 (negative) to 1 (positive)
    """
    Analyzes the sentiment of the input text.

    Parameters:
    text (str): The text to analyze.

    Returns:
    float: Sentiment score ranging from -1 (negative) to 1 (positive).
    """
# Apply sentiment analysis on the cleaned data
df['sentiment'] = df['cleaned_message'].apply(analyze_sentiment)
df.to_csv('sentiment_messages.csv', index=False)
print("Sentiment analysis complete. Data saved to 'sentiment_messages.csv'.")
