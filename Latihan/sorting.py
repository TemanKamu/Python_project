import random
var_list = [random.randint(1, 100) for i in range(0, 101)]
left_pointer = var_list[0]
number = list()
for i in range(1,len(var_list)):
    for r in range(1, len(var_list)):
        right_pointer = var_list[r]
        if right_pointer > left_pointer:
            for x in range(0, len(number)):
                if number[x] == right_pointer:
                    break
            else:
                left_pointer = right_pointer
    if left_pointer not in number and left_pointer != var_list[0]:
        number.append(left_pointer)
        left_pointer = var_list[0]
print(number)
print(var_list)

"""
 1. Perulangan pada blok pertama melakukan iterasi sebanyak 100x agar pada perulangan
    sangkar kedua selalu mencari bilangan terbesar
 2. Perluangan pada blok kedua fungsinya untuk mencari bilangan terbesar
 3. Perulangan pada blok ketiga fungsinya mencek apakah bilangan terbesar yang sudah
    terpilih sudah ada di array kumpulan bilangan terbesar

"""