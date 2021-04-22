slice=int(input("How many pizza slice you want = "))
if slice%2==0:
    price=slice*120
    print("Total amount =",price)
else:
    price=slice*123
    print("Total amount =",price)