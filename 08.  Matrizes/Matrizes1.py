N = int(input())
M = int(input())

matriz = []

for i in range (N):
    l = []    
    
    if i == 0:
        maior = int(input())
        l.append(maior) 
        for _ in range (1,M):
            a = int(input())
            l.append(a)
            if a > maior:
                maior = a            
    else:
        for _ in range (M):
            a = int(input())
            l.append(a)    
            if a > maior:
                maior = a
        
    matriz.append(l)
    
for i in range (N):
    for j in range (M):
        matriz[i][j] -= maior
    
print(matriz)