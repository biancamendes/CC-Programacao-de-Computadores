for i in range (100, 1000):
    
    c = int(i/100)
    d = int((i-c*100)/10)
    u = int(i-d*10-c*100)
    
    if(c**3 + d**3 + u**3 == i):
        print(i)