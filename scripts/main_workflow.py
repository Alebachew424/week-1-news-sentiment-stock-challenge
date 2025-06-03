import os
import seaborn as sns
import pandas as pd

# Set plot style
sns.set(style='whitegrid')

# Define the base directory for your data
base_data_path = r"D:\Tnx_Week1\week-1-news-sentiment-stock-challenge\Data\Data"

# Paths to your data files
NEWS_DATA_PATH = os.path.join(base_data_path, 'raw_analyst_ratings', 'raw_analyst_ratings.csv')
TSLA_PATH = os.path.join(base_data_path, 'yfinance_data', 'yfinance_data', 'TSLA_historical_data.csv')
NVDA_PATH = os.path.join(base_data_path, 'yfinance_data', 'yfinance_data', 'NVDA_historical_data.csv')
MSFT_PATH = os.path.join(base_data_path, 'yfinance_data', 'yfinance_data', 'MSFT_historical_data.csv')
META_PATH = os.path.join(base_data_path, 'yfinance_data', 'yfinance_data', 'META_historical_data.csv')
GOOG_PATH = os.path.join(base_data_path, 'yfinance_data', 'yfinance_data', 'GOOG_historical_data.csv')
AMZN_PATH = os.path.join(base_data_path, 'yfinance_data', 'yfinance_data', 'AMZN_historical_data.csv')

# Load your data
try:
    news_df = pd.read_csv(NEWS_DATA_PATH)
    print("News Data:")
    print(news_df.head())

    tsla_df = pd.read_csv(TSLA_PATH)
    print("\nTSLA Data:")
    print(tsla_df.head())

    nvda_df = pd.read_csv(NVDA_PATH)
    print("\nNVDA Data:")
    print(nvda_df.head())

    msft_df = pd.read_csv(MSFT_PATH)
    print("\nMSFT Data:")
    print(msft_df.head())

    meta_df = pd.read_csv(META_PATH)
    print("\nMETA Data:")
    print(meta_df.head())

    goog_df = pd.read_csv(GOOG_PATH)
    print("\nGOOG Data:")
    print(goog_df.head())

    amzn_df = pd.read_csv(AMZN_PATH)
    print("\nAMZN Data:")
    print(amzn_df.head())

except FileNotFoundError as e:
    print(f"Error: {e}")