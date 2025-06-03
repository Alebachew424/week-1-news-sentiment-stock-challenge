# scripts/correlation_analysis.py

from scipy.stats import pearsonr

def compute_correlation(df, stock_symbol):
    df_stock = df[df['stock'] == stock_symbol].dropna(subset=['sentiment_score', 'daily_return'])
    if len(df_stock) < 2:
        print(f"{stock_symbol}: Not enough data for correlation.")
        return None
    corr, p_value = pearsonr(df_stock['sentiment_score'], df_stock['daily_return'])
    print(f"{stock_symbol}: Correlation={corr:.3f}, p-value={p_value:.3f}")
    return corr, p_value