N = int(input())

A = []

for _ in range (N):
    l = []        
    for _ in range (N):
        a = int(input())
        l.append(a)         
    A.append(l)

sum  = 0
cont = 0

for i in range (N):
    for j in range (N):
        if (j > i and j < N-i-1) or (j > N-i-1 and j < i):
            sum  += A[i][j]
            cont += 1    
    
print ('%.2f'%(sum/cont))