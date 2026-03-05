jumlah_baris = 15
def pascal_pattern(row):
    list_bilangan_segitiga_pascal = [[0,1,0]]
    for i in range(0, row - 1):
        temp = list()
        for j in range(0, len(list_bilangan_segitiga_pascal[i])):
            if j == 0:
                temp.append(0)
            else:
                temp.append(list_bilangan_segitiga_pascal[i][j] + list_bilangan_segitiga_pascal[i][j - 1])
        temp.append(0)
        list_bilangan_segitiga_pascal.append(temp)
    return list_bilangan_segitiga_pascal


pascal = pascal_pattern(jumlah_baris)
space = jumlah_baris
for i in range(0, len(pascal)):
    text = " "
    text_each_row = []
    for j in pascal[i]:
        if j != 0:
            text_each_row.append(str(j))
    print(text.join(text_each_row).rjust(space))
    for l in range(0, space):
        # 
        if l % 5 == 0:
            space += 1
    # print(space)