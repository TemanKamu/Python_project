"""
User Menabung dengan jumlah yang sama setiap harinya maka b (beda) sifatnya konstan
User tidak perlu memberi informasi berapa nominal ia menabung setiap periode
User hanya perlu memberi informasi minimal 2 data mengenai nominal tabungan
yang dimasukkan setiap bulannya

Maka dari permasalahan tersebut kita bisa menggunakan deret aritmatika untuk penyelesaiannya
"""
data_tabungan = list()
for i in range (0,2):
    input_data = int(input(f"Masukkan jumlah tabungan pada Periode-{ i + 1}: "))
    data_tabungan.append(input_data)

n = int(input("Masukkan Periode berapa yang ingin anda ketahui total tabungan ada pada periode tersebut: "))

a = data_tabungan[0]
b = data_tabungan[1] - a

sn = int(n/2 * ((2 * a) + (n - 1) * b))

print(f"Pada Periode-{n}, Total tabungan anda adalah Rp{sn} dan jumlah menabung setiap periode adalah Rp{b}")