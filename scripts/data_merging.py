# scripts/data_merging.py

import pandas as pd

def aggregate_daily_sentiment(df_news):
    return df_news.groupby(['publication_date', 'stock'])['sentiment_score'].mean().reset_index()

def merge_with_stock(df_stock, df_sentiment, stock_symbol):
    df_stock_reset = df_stock.reset_index()
    df_stock_reset['date'] = df_stock_reset['Date'].dt.date
    df_stock_sym = df_sentiment[df_sentiment['stock'] == stock_symbol]
    merged = pd.merge(df_stock_reset, df_stock_sym, left_on='date', right_on='publication_date', how='left')
    merged['sentiment_score'].fillna(0, inplace=True)
    return merged