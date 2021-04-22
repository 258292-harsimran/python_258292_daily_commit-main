tup1=(1,0,4,5,5,5,3)  
print(tup1)
for i in tup1:
    if tup1.count(i) > 1:
        print("repeated item is=",i)
        break