N = int(input())

A  = []
B  = []
At = []
C  = []

for _ in range (N):
    l = []        
    for _ in range (N):
        a = int(input())
        l.append(a)        
    A.append(l)

for _ in range (N):
    B.append([0]*N)
    At.append([0]*N)
    C.append([0]*N)
    
    
for i in range (N):
    for j in range (N):
        for k in range (N):
            B[i][j]=B[i][j]+(A[i][k]*A[k][j])
            
for i in range (N):      
    for j in range (N):
        At[i][j],At[j][i]=A[j][i],A[i][j]

for i in range (N):      
    for j in range (N):
        C[i][j] = B[i][j]+At[i][j]

print(C)