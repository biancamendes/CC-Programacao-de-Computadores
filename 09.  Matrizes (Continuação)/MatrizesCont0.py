N = int(input())
M = int(input())
v = [0]*(N*M)

for i in range (N*M):
    v[i] = int(input())

for _ in range (N*M):
    for i in range ((N*M)-1):
        if (v[i]<v[i+1]):
            v[i],v[i+1]=v[i+1],v[i]

A = []
for i in range(N):
    l = []
    for j in range(M):
        l.append(v[i+N*j])
    A.append(l) 
            
print(A)