import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from textblob import TextBlob

def load_csv(file_path, parse_dates=None):
    return pd.read_csv(file_path, parse_dates=parse_dates)

def preprocess_dates(df, date_col):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df.dropna(subset=[date_col], inplace=True)
    return df

def extract_domain(publisher):
    match = re.search(r'@([\w.-]+)', str(publisher))
    return match.group(1) if match else publisher

def get_headlines(df, text_col='headline'):
    return df[text_col].fillna('')

def compute_sentiment(texts):
    return texts.apply(lambda x: TextBlob(x).sentiment.polarity)

def perform_topic_modeling(texts, max_features=1000, n_topics=5):
    vectorizer = CountVectorizer(stop_words='english', max_features=max_features)
    dtm = vectorizer.fit_transform(texts)
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(dtm)
    return lda, vectorizer

def get_top_words(lda, vectorizer, n_top=10):
    topics = []
    for idx, topic in enumerate(lda.components_):
        top_indices = topic.argsort()[-n_top:][::-1]
        words = [vectorizer.get_feature_names_out()[i] for i in top_indices]
        topics.append(words)
    return topics