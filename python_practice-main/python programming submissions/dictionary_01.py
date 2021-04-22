d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
print(d1)
print(d2)

d = d1.copy()
d.update(d2)
print("Merged Dictonary=",d)
