datas = ["  BTC, 43000 ", "ETH,  3000", " SOL ,150 ", "ADA,   1.2  "]
datasFormatted = dict()


for data in datas:
    localData = data.strip().split(',')
    datasFormatted[str(localData[0]).strip()] = float(localData[1].strip())

print(datasFormatted)