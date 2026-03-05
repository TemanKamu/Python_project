# lstrip() adalah metode string yang digunakan untuk menghapus karakter tertentu di bagian kiri (awal) dari string.
kata = "   Hello, World!  "
print("Output dari metode lstrip(): ", kata.lstrip())

# rstrip() adalah metode yang digunakan untuk menghapus karakter tertentu di bagian kanan (akhir) dari string.
kata = "  Hello, World!    "
print("Output dari metode rstrip(): ", kata.rstrip())

# strip() adalah metode yang digunakan untuk menghapus karakter tertentu di sebelah kanan dan kiri (awal dan akhir) dari string
kata = "   Hello, World!   "
print("Output dari metode strip(): ", kata.strip())

# Untuk menghapus karakter selain whitespace anda bisa masukkan karakter yang ingin anda masukkan ke dalam argument
kata = "Hello, World!"
print("""Output dari metode .strip() untuk menghapus karakter selain whitespace:
      """, kata.strip("World!"))

# Untuk mencari karakter tertentu kita bisa menggunakan metode startswith() dan endswith()
# Output akan berupa boolean yaitu True jika ada, False kalau tidak ada
kata = "Hello, Dunia!"
# startswith()
print("Output dari metode .startswith(): ", kata.startswith("Hello"))
# endswith()
print("Output dari metode .endswith(): ", kata.endswith("Dunia!"))


# Menggabungkan dan memisahkan string bisa menggunakan metode .join dan .split

# .join() menggabungkan kumpulan string yang ada di dalam list
kata = " ".join(["Halo", "Lutfi!"])
# " " digunkana sebagai delimiter atau pembatas untuk format teks, karena ada 2 string yang ingin digabungkan
# maka perlu pembatas agar kalimat tidak menyatu dan disini menggunkan white space
print(kata)

# .split() berbeda dengan join(), metode .split() digunkana untuk memisah setiap kalimat yang ada di dalam string 
# berdasarkan delimiter
kata = "Nama saya adalah lutfi agisna"
print(kata.split(" "))

# Pengecekan String
# isupper() untuk mencek apakah setiap huruf yang ada di dalam string apakah huruf besar.
kata = "NAMA SAYA LUTFI DAN UMUR SAYA 20 TAHUN"
print(kata.isupper())

# islower() adalah kebalikan dari isupper()
kata = "nama saya adalah lutfi dan umur saya 20 tahun"
print(kata.islower())

# istitle() untuk mencek apakah karatker pertama pada sebuah kalimat itu kapital atau tidak
kata = "Nama Saya Adalah Lutfi Agisna Dan Umur Saya 20 Tahun"
print(kata.istitle())

# isalpa() digunakan untuk mencek apakah seluruh karakter yang ada didalam string adalah alfabet
print("LutfiAgisna".isalpha())

# isnumeric() digunakan untuk mencek apakah seluruh karakter yang ada didalam string adalah number
print("1234".isnumeric())

# isalnum() digunkakan untuk mencek apakah seluruh karakter yang ada didalam string ada alfabet dan number
print("Umur20".isalnum())

# isdecimal() digunakna untuk mencek apakah seluruh karakter yang ada didalam string adalah numerik / angka
print("123".isdecimal())

# isspace() digunakan untu mencek apakah seluruh karakter yang ada didalam string adalah spasi
print("   ".isspace())

# Format teks
# .zfill() digunakan untuk membuat panjang string menjadi tetap dengan cara memasukkan angka 0 dibelakang kalimat
kata = "Rusdi"
# Membuat panjang string yang ada didalam variabel kata menjadi 10 karakter
tambah_kata = kata.zfill(10)
print(tambah_kata)

# ljust() digunakan untuk membuat teks yang ada didalam string menjadi rata kiri dengan menambahkan karakter dengan
# jumlah tertentu di sebelah kanan
kata = "Rusdi"
tambah_kata = kata.ljust(20, "!")
print(tambah_kata)

# rjust() digunakan untuk membuat teks yang ada didalam string menjadi rata kanan dengan menambahkan karakter dengan
# jumlah tertentu kesebelah kiri
kata = "Rusdi"
tambah_kata = kata.rjust(20,"!")
print(tambah_kata)

# center() digunakna untuk membuat teks yang ada didalam string berada di tengah dengan menambahkan karakter dalam jumlah
# tertentu di sebelah kanan dan krii

kata = "Lutfi"
tambah_kata = kata.center(20," ")
print(tambah_kata)