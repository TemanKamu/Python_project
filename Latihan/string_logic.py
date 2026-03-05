data = "2024-01-01,BTC,43000".split(',')

# Formatted data
formattedData = {
    "date": data[0],
    "symbol": data[1],
    "price": int(data[2])
}

print(formattedData)