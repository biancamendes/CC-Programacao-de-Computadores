def minimo(N, v, a, b):
    
    menor  = v[a]
    imenor = a
    
    for i in range (a+1, b+1):
        if v[i] < menor:
            menor  = v[i]
            imenor = i
        
    return imenor

N = int(input())

v = [0]*N
for i in range (N):
    v[i] = int(input())

M = int(input())

for i in range (M):
    a = int(input())
    b = int(input())    
    indice = minimo(N, v, a, b)
    
    print(int(indice))