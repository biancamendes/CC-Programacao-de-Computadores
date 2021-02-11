A = int(input())
B = int(input())

for i in range (A,B+1):
    primo = 0
    for j in range (2,int(i/2)+1):
        if (i%j == 0):
            primo = 1
            
    if primo == 0:
        c = int(i/100)
        d = int((i-c*100)/10)
        u = int(i-d*10-c*100)
        
        if (c+d+u)%2 == 0:        
            print(i)