# scripts/stock_analysis.py

def compute_daily_returns(df):
    df['daily_return'] = df['Close'].pct_change()
    return df