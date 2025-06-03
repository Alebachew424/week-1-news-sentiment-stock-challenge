import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

def plot_publication_trend(counts):
    plt.figure(figsize=(12,6))
    counts.plot()
    plt.title('Number of Articles Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.show()

def plot_article_time_distribution(df):
    if 'publication_time' in df.columns:
        df['pub_hour'] = pd.to_datetime(df['publication_time']).dt.hour
        plt.figure(figsize=(10,6))
        sns.countplot(x='pub_hour', data=df)
        plt.title('Articles Published by Hour of Day')
        plt.xlabel('Hour of Day')
        plt.ylabel('Number of Articles')
        plt.show()

def plot_stock_price(df, ticker):
    plt.figure(figsize=(14,7))
    plt.plot(df['Close'], label='Close Price')
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()