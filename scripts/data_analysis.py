import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define your base directory
base_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))

# Update file paths based on your structure
files = {
    'news': os.path.join(base_dir, 'Data', 'Data', 'raw_analyst_ratings', 'raw_analyst_ratings.csv'),
    'tsla': os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'TSLA_historical_data.csv'),
    'nvda': os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'NVDA_historical_data.csv'),
    'msft': os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'MSFT_historical_data.csv'),
    'meta': os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'META_historical_data.csv'),
    'goog': os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'GOOG_historical_data.csv'),
    'amzn': os.path.join(base_dir, 'Data', 'Data', 'yfinance_data', 'yfinance_data', 'AMZN_historical_data.csv')
}

# Load datasets
news_df = pd.read_csv(files['news'])
tsla_df = pd.read_csv(files['tsla'])
nvda_df = pd.read_csv(files['nvda'])
msft_df = pd.read_csv(files['msft'])
meta_df = pd.read_csv(files['meta'])
goog_df = pd.read_csv(files['goog'])
amzn_df = pd.read_csv(files['amzn'])

# 1. Data Validation - Check for missing values
datasets = {
    'News Data': news_df,
    'TSLA Data': tsla_df,
    'NVDA Data': nvda_df,
    'MSFT Data': msft_df,
    'META Data': meta_df,
    'GOOG Data': goog_df,
    'AMZN Data': amzn_df
}

print("Missing Data Summary:")
for name, df in datasets.items():
    missing = df.isnull().sum()
    print(f"\n{name}:")
    print(missing[missing > 0])

# 2. Convert 'Date' columns to datetime
for df in [tsla_df, nvda_df, msft_df, meta_df, goog_df, amzn_df]:
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    elif 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

# 3. Visualize Stock Price Trends
def plot_stock(df, stock_name):
    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['Close'], label=stock_name)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title(f'{stock_name} Stock Price Over Time')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Plot TSLA
plot_stock(tsla_df, 'TSLA')
# You can add similar plots for other stocks as needed.

# 4. Merge Stock Data with News Data
# Ensure date columns are datetime
if 'date' in news_df.columns:
    news_df['date'] = pd.to_datetime(news_df['date'])
if 'Date' in tsla_df.columns:
    tsla_df['Date'] = pd.to_datetime(tsla_df['Date'])

# Merge example for TSLA
merged_tsla_news = pd.merge(tsla_df, news_df, left_on='Date', right_on='date', how='inner')
print("Merged TSLA Stock Data with News:")
print(merged_tsla_news.head())

# Save merged data if needed
merged_tsla_news.to_csv('merged_tsla_news.csv', index=False)

# 5. Analyze Relationship: Headline Length vs Stock Price Change
if 'headline' in news_df.columns and 'Close' in tsla_df.columns:
    # Create a headline length feature
    news_df['headline_length'] = news_df['headline'].astype(str).apply(len)

    # Merge again for analysis
    merged = pd.merge(tsla_df, news_df[['date', 'headline_length']], left_on='Date', right_on='date', how='inner')
    merged['Price Change'] = merged['Close'].diff()

    plt.figure(figsize=(10,6))
    sns.scatterplot(x='headline_length', y='Price Change', data=merged)
    plt.title('Headline Length vs Stock Price Change')
    plt.xlabel('Headline Length')
    plt.ylabel('Price Change')
    plt.tight_layout()
    plt.show()

    corr = merged[['headline_length', 'Price Change']].corr().iloc[0,1]
    print(f"Correlation between headline length and price change: {corr:.2f}")

# 6. Save visualizations if needed
# plt.savefig('headline_vs_price_change.png')

print("Analysis completed.")