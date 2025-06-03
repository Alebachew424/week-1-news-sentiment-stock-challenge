import os
import seaborn as sns
import pandas as pd

# Optional: Uncomment if you want to use pandas_ta instead of TA-Lib
# import pandas_ta as ta

# Set seaborn plot style
sns.set(style='whitegrid')

# Define the base directory (parent directory of current working directory)
base_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))

# Paths to your data files
NEWS_DATA_PATH = os.path.join(base_dir, 'Data', 'Data', 'raw_analyst_ratings', 'raw_analyst_ratings.csv')
TSLA_PATH = os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'TSLA_historical_data.csv')
NVDA_PATH = os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'NVDA_historical_data.csv')
MSFT_PATH = os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'MSFT_historical_data.csv')
META_PATH = os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'META_historical_data.csv')
GOOG_PATH = os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'GOOG_historical_data.csv')
AMZN_PATH = os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'AMZN_historical_data.csv')

# Load datasets with error handling
try:
    news_df = pd.read_csv(NEWS_DATA_PATH)
    print("Raw Analyst Ratings Data:")
    print(news_df.head())

    tsla_df = pd.read_csv(TSLA_PATH)
    print("\nTSLA Historical Data:")
    print(tsla_df.head())

    nvda_df = pd.read_csv(NVDA_PATH)
    print("\nNVDA Historical Data:")
    print(nvda_df.head())

    msft_df = pd.read_csv(MSFT_PATH)
    print("\nMSFT Historical Data:")
    print(msft_df.head())

    meta_df = pd.read_csv(META_PATH)
    print("\nMETA Historical Data:")
    print(meta_df.head())

    goog_df = pd.read_csv(GOOG_PATH)
    print("\nGOOG Historical Data:")
    print(goog_df.head())

    amzn_df = pd.read_csv(AMZN_PATH)
    print("\nAMZN Historical Data:")
    print(amzn_df.head())

except FileNotFoundError as e:
    print(f"File not found: {e}")

except pd.errors.EmptyDataError as e:
    print(f"Empty data error: {e}")

except pd.errors.ParserError as e:
    print(f"Parsing error: {e}")