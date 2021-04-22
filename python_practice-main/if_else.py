year=int(input())

if year % 400 == 0 and year % 4 == 0:
    print("its a leap year")
else :
    print("its not a leap year")