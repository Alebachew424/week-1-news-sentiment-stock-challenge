import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import (
    load_csv, preprocess_dates, extract_domain,
    get_headlines, compute_sentiment, perform_topic_modeling,
    get_top_words
)

# Set style
sns.set(style='whitegrid')

# Define data paths
base_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
paths = {
    'News Data': os.path.join(base_dir, 'Data', 'Data', 'raw_analyst_ratings', 'raw_analyst_ratings.csv'),
    'TSLA': os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'TSLA_historical_data.csv'),
    # Add other stocks paths
}

# Load news data
news_df = load_csv(paths['News Data'])
news_df = preprocess_dates(news_df, 'date')
news_df['publication_date'] = news_df['date'].dt.date

# Extract domain
news_df['domain'] = news_df['publisher'].apply(extract_domain)

# Text analysis
headlines = get_headlines(news_df, 'headline')

# Topic modeling
lda, vectorizer = perform_topic_modeling(headlines)
topics = get_top_words(lda, vectorizer)
for idx, topic in enumerate(topics):
    print(f"Topic {idx+1}: {', '.join(topic)}")

# Sentiment analysis
news_df['sentiment_score'] = compute_sentiment(headlines)

# Plot sentiment over time
daily_sentiment = news_df.groupby('publication_date')['sentiment_score'].mean().reset_index()

# (Load stock data similarly and merge with sentiment for correlation)

# ... Continue with analysis, visualization, and correlation calculations