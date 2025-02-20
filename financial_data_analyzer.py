import yfinance as yf
import matplotlib.pyplot as plt

def analyze_stock(ticker):
    # Download 6 months of historical data for the given ticker
    data = yf.download(ticker, period="6mo")
    # Calculate a 50-day moving average
    data['MA50'] = data['Close'].rolling(window=50).mean()
    
    # Plot the closing price and moving average
    plt.figure(figsize=(10,5))
    plt.plot(data['Close'], label="Close Price")
    plt.plot(data['MA50'], label="50-Day MA", linestyle='--')
    plt.title(f"{ticker} Stock Price Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g., AAPL): ")
    analyze_stock(ticker)
