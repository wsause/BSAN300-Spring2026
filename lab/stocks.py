import yfinance as yf

ticker = yf.Ticker("META")
data = ticker.history(period="1d")
print(data)