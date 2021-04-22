list = [1, 2, 3, 4]
dict = current = {}
print("list=",list)
print("dictionary=",dict)
for n in list:
    current[n] = {}
    current = current[n]
print(dict)