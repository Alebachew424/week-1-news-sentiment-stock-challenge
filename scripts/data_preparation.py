# scripts/data_preparation.py

import pandas as pd
import os

def load_news_data(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['date'], inplace=True)
    df['publication_date'] = df['date'].dt.date
    return df

def load_stock_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    return df

# Example usage:
# news_df = load_news_data('data/raw/financial_news.csv')
# tsla_df = load_stock_data('data/raw/TSLA_historical_data.csv')