# Python3 code to demonstrate
# Split list into lists by particular value
# Using list comprehension + zip() + slicing + enumerate()
  
# initializing list
test_list = ['Mes', 2022, 2021, "\n", 2020, 2019, "\n", 2018, 2017, 2016, 2015, 2016, 2017]

# printing original list
print("The original list : " + str(test_list))
  
# using list comprehension + zip() + slicing + enumerate()
# Split list into lists by particular value
size = len(test_list)
idx_list = [idx + 1 for idx, val in
            enumerate(test_list) if val == "\n"]
  
  
res = [test_list[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[-1] != size else []))]
  
# print result
print("The list after splitting by a value : " + str(res))
try:
    print("Esto en res[0] = ",res[0], "y su tipo es: ", type(res[0]), "y su longitud es: ", len(res[0]))
except: 
    pass
try:
    print("Esto es res[1] = ", res[1], "y su tipo es: ", type(res[1]), "y su longitud es: ", len(res[1]))
except:
    pass
try:
    print("Esto es res[2] = ", res[2],  "y su tipo es: ", type(res[2]), "y su longitud es: ", len(res[2]))
except:
    pass
print("El resultado final es de tipo: ", type(res), " y su longitud es: ", len(res))