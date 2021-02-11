N = int(input())
S = i = 0

for x in range (1,201,4):
    
    i += 1
    
    if i%2 != 0:
        S += x+N
    else:
        S += x*N
        
print (S)  