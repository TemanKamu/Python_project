jumlah_suku = 5
list_bilangan_segitiga = list()

for i in range(1, jumlah_suku + 1):
    list_bilangan_segitiga.append(int((i * (i + 1))/2))
print(list_bilangan_segitiga)