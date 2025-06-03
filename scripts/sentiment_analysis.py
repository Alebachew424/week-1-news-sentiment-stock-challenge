# scripts/sentiment_analysis.py

from textblob import TextBlob

def add_sentiment_scores(df):
    df['sentiment_score'] = df['headline'].astype(str).apply(lambda x: TextBlob(x).sentiment.polarity)
    return df