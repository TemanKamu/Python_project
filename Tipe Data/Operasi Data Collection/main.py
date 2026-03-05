# fungsi len digunakan untuk mengetahui jumlah item yang ada didalam list
bilangan = [1,2,3,4,4,5,6,7,7]
print("Panjang List: ",len(bilangan))

himpunanBilangan = set(bilangan)
print("Panjang himpunan: ",len(himpunanBilangan))

# min() digunakan untuk mengetahui nilai terkecil yang ada didalam list
# max() digunakan untuk mengehahui nilai terbesar yang ada didalam list
print("Nilai Terkecil: ", min(bilangan))
print("Nilai Terbesar: ", max(bilangan))

# .count() digunakan untuk berapa jumlah karakter tertentu yang ada didalam list
print("Item dengan data 7 ada sebanyak ",bilangan.count(7), "item di dalam list") 

# in digunakan untuk mencek apakah ada karakter tertentu yang ada dialam list dan objek
print("Apakah ada bilangan 1 ?", 1 in bilangan)
# not in digunakan untuk mencek apakah tidak ada karakter tertentu yang ada didalam list dan objek
print("Apakah tidak ada kalimat 'Nama'?","Nama" not in "Nama saya adalah lutfi")

# Multi Variable digunakan untuk inisialisasi banyak variabel dengan list
biodata = ["Lutfi", "Pria", 20]
nama,jenis_kelamin,umur = biodata
print("Nama: ", nama)
print("Jenis Kelamin: ", jenis_kelamin)
print("Umur: ", umur)

# .sort() digunakan untuk mengurutkan karakter, defaultnya dari terkecil ke terbesar
newBilangan = bilangan.copy()
# Dari terbesar ke terkecil
newBilangan.sort(reverse=True)
print(newBilangan)
