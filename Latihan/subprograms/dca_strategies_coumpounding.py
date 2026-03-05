capital = float(input("Masukkan Jumlah Modal Anda: "))
deposit = float(input("Masukkan Jumlah Deposit per Periode: "))
numberPeriods = int(input("Masukkan Jumlah Periode: "))
returnPeriods = float(input("Masukkan jumlah return per bulan (%): "))

def initial_capital_compounding(capital, numberPeriods, returnPeriods):
    totalReturn = capital * (1 + returnPeriods/100)**numberPeriods
    return totalReturn

def deposit_compounding(deposit, numberPeriods, returnPeriods):
    totalReturn = deposit * (1 + returnPeriods/100)**numberPeriods
    return totalReturn

print("-------------------------------------------------")
capitalReturn = capital
depositReturn = 0
totalMoney = 0
for i in range(0, numberPeriods+1):
    capitalReturn = initial_capital_compounding(capital,i,returnPeriods)
    if i != 0:
         for j in range((i-1), -1, -1):
             if i == numberPeriods and j == 0:
                 break
             depositReturn += deposit_compounding(deposit, j, returnPeriods)
    print(f"Bulan ke-{i} Total Return: {capitalReturn + depositReturn}")
    totalMoney = capitalReturn + depositReturn
    if i != numberPeriods:
        depositReturn = 0
print("-------------------------------------------------")
print(f"Modal Awal: {capital}")
print(f"Total Modal Investasi (Modal + Deposit): {capital + deposit*numberPeriods - 1}")
# print(f"Return Total: (%): {totalMoney/capital + deposit*numberPeriods * 100}%")
print(f"Return Total: {int(totalMoney - (capital + deposit*numberPeriods))}")
"""
Input:
    - Modal Awal
    - Deposit Per Periode
    - Jumlah Periode
Output:
    - Return per Periode: Total Modal + Return
    - Return Total (%) 
    - Return Total (Jt) 
"""