import yfinance as fy

def get_data(tickers, start_date, end_date):
    return fy.download(tickers, start_date, end_date)['Adj Close']

