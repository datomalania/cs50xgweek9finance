#საჭიროა ბიბლიოთეკის ინსტალაცია
# pip install yfinance
# ეს კოდი არ არის ფინანსების დავალების ნაწილი
# Enter share name: nvda
# last market price NVDA: 115.0690000000069242
# აქციების დასახელებები AAPL, AMZN, TSLA, A




import yfinance as yf
STK = input("Enter share name: " ).upper()
data = yf.Ticker(STK).history(period="1d")
last_market_price = data['Close'].iloc[-1]
print(f"last market price {STK}:", last_market_price)

#source code  -->https://medium.com/@splashproject2080/qunat-analysis-series-1-download-live-and-historical-stock-data-a-complete-tutorial-91b5eaf78321
