var_array = [i for i in range(0,101)]
result = 0
for i in range(0, len(var_array)):
    counter = i + 1
    if counter < len(var_array):
        result += var_array[counter]
    else:
        result /= len(var_array)