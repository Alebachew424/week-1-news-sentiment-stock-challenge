import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(stock_path, sentiment_path):
    # Check if files exist
    if not os.path.exists(stock_path):
        print(f"Stock Data file not found at {stock_path}")
        return None
    if not os.path.exists(sentiment_path):
        print(f"Sentiment Data file not found at {sentiment_path}")
        return None

    # Load data
    stock_df = pd.read_csv(stock_path, parse_dates=['Date'])
    sentiment_df = pd.read_csv(sentiment_path, parse_dates=['Date'])

    # Merge on Date
    merged_df = pd.merge(stock_df, sentiment_df, on='Date', how='inner')
    return merged_df

def compute_indicators(df):
    # Ensure data is sorted
    df = df.sort_values('Date').reset_index(drop=True)

    # Calculate 7-day and 21-day moving averages
    df['MA_7'] = df['Close'].rolling(window=7).mean()
    df['MA_21'] = df['Close'].rolling(window=21).mean()

    # Calculate Bollinger Bands
    df['Std_7'] = df['Close'].rolling(window=7).std()
    df['Upper_Band'] = df['MA_7'] + 2 * df['Std_7']
    df['Lower_Band'] = df['MA_7'] - 2 * df['Std_7']

    # Calculate RSI
    delta = df['Close'].diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    roll_up = up.rolling(14).mean()
    roll_down = down.rolling(14).mean()
    RS = roll_up / roll_down
    df['RSI'] = 100 - (100 / (1 + RS))

    # Handle NaN values
    df.fillna(method='bfill', inplace=True)

    return df

def plot_stock_with_indicators(df):
    plt.figure(figsize=(14, 8))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['MA_7'], label='7-Day MA', color='orange')
    plt.plot(df['Date'], df['MA_21'], label='21-Day MA', color='green')
    plt.plot(df['Date'], df['Upper_Band'], label='Upper Bollinger Band', color='red', linestyle='--')
    plt.plot(df['Date'], df['Lower_Band'], label='Lower Bollinger Band', color='red', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Tesla Stock Price with Moving Averages and Bollinger Bands')
    plt.legend()
    plt.show()

def main():
    # Define your base directory (adjust if needed)
    base_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))

    # Correct paths based on your provided structure
    stock_data_path = os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'TSLA_historical_data.csv')
    sentiment_data_path = os.path.join(base_dir, 'Data', 'Data', 'raw_analyst_ratings', 'raw_analyst_ratings.csv')

    # Verify paths
    print("Stock data path:", stock_data_path)
    print("Sentiment data path:", sentiment_data_path)

    # Load data
    data = load_data(stock_data_path, sentiment_data_path)
    if data is None:
        return

    # Compute indicators
    data_with_indicators = compute_indicators(data)

    # Display the last few rows
    print(data_with_indicators.tail())

    # Plot stock with indicators
    plot_stock_with_indicators(data_with_indicators)

if __name__ == "__main__":
    main()