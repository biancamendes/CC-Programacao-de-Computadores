X = int(input())
S = X
i = 2

for n in range (3,498,5):
    
    i += 1
    
    if i%2 != 0:
        S += (n*X)/(2*i+1)
    else:
        S -= (n*X)/(2*i+1)
        
print ('%.3f'%S)