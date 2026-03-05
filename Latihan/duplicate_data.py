# Duplicate Data
trades = ["BTC", "ETH", "BTC", "SOL", "ETH", "ADA"]
duplicateName = list()
for pairName in trades:
    if trades.count(pairName) > 1:
        duplicateName.append(pairName)

print("Data Duplikat: ", duplicateName)


# Unique Data
uniqueData = list()
for x in range(0,len(trades)):
    for y in range(x+1, len(trades)):
        if trades[x] == trades[y]:
            uniqueData.append(trades[y])
    if trades.count(trades[x]) <= 1:
        uniqueData.append(trades[x])
print("Data Unik: ", uniqueData)

# Frecuency Data
trades = ["BTC", "ETH", "BTC","ETH", "SOL", "ETH","ETH", "ADA", "BTC"]
uniqueData = dict()
for x in range(0,len(trades)):
    for y in range(x+1, len(trades)):
        if trades[x] == trades[y]:
            counter = 0
            for p in trades:
             if trades[x] == p:
                 counter += 1
            uniqueData[str(trades[y])] = counter
    if trades.count(trades[x]) <= 1:
        counter = 0
        for p in trades:
            if trades[x] == p:
                counter += 1
        uniqueData[str(trades[x])] = counter
print("Frekuensi Data: ",uniqueData)

# Data terbanyak
for x in range(0, len(trades)):
    for y in range(x+1, len(trades)):
        if trades.count(trades[y]) > trades.count(trades[x]):
            print("Data Terbanyak:", [trades[y]])
            break
    break


