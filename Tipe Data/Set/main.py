""" Set memiliki definisi yang sama seperti himpunan dalam matematika, yaitu kumpulan objek atau elemen yang
 saling berkaitan dan memiliki karakteristik yang sama lalu dikelompokkan dalam satu kesatuan. Memiliki aturan 
yang sama dengan himpunan matematika, yaitu tidak memiliki elemen yang sama (tidak duplikat)"""

# Set tidak dapat melakukan indexing atau slicing karena set tidak memiliki urutan (unordered).
bilanganBulat = {1,2,3,4,5}
bilanganGanjil = {1,3,5,7,9}

# Melakukan penggabungan himpunan dengan operator union (|) atau metode union()
gabunganHimpunan = bilanganBulat.union(bilanganGanjil)
print("Gabungan himpunan bilangan bulat dan ganjil:", gabunganHimpunan)

# Irisan himpunan dengan operator intersection (&) atau metode intersection()
irisanHimppunan = bilanganBulat.intersection(bilanganGanjil)
print("Irisan himpunan bilangan bulat dan ganjil:", irisanHimppunan)