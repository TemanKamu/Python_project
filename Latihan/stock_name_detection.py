symbols = ["AAPL", "TSLA1", "GOOG", "BTC!", "MSFT"]

validName = list()

for symbol in symbols:
    if(symbol.isalpha()):
        validName.append(symbol)

print(validName)