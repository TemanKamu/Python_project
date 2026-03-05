# Simplenya Dictionary itu seperti kamus yang berisi kumpulan kata dan artinya.
# Sebuah data yang ada di dalam dictionary disebut sebagai item, dimana setiap item terdiri
# dari key dan value. key adalah kunci yang dignakan untuk mengakses value, sedangkan value adalah nilai yang terkait dengan key tersebut.
biodata = {
    "nama": "John Doe",
    "umur": 30,
    "pekerjaan": "Software engineer"
}

# Mengakses nilai dalam dictionary menggunakan key
print(f"Nama: {biodata['nama']}")

# Mengubah value dalam dictionary menggunakan key
biodata["umur"] = 31
print(f"Umur setelah diubah: {biodata['umur']}")

# Mennambahkan item baru ke dalam dictionary
biodata['tanggalLahir'] = "1 Januari 1990"
print("Biodata setelah menambahkan tanggal lahir:", biodata)

# Menghhapus item dari dictionary menggunakan del
del biodata['tanggalLahir']
print("Biodata setelah menghapus tanggal lahir:", biodata)