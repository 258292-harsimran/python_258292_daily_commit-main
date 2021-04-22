def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
      
# Driver Code    
tups = [("med1", 10), ("med2", 20), ("med3", 30), 
     ("med4", 40), ("med5", 50), ("med6", 60)]
dictionary = {}
print("list of tuples converted to dictionary")
print (Convert(tups, dictionary))