jumlah_suku = 10

bilangan_fibonacci = [0,1,1]

for i in range(len(bilangan_fibonacci), jumlah_suku):
    hasil = bilangan_fibonacci[i - 1] + bilangan_fibonacci[i - 2]
    bilangan_fibonacci.append(hasil)

print(bilangan_fibonacci)