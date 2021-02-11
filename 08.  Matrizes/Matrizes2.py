N = int(input())

matriz = []

for _ in range (N):
    l = []    
    
    for _ in range (N):
        a = int(input())
        l.append(a)    
        
    matriz.append(l)
    
for i in range (N):
    matriz[i][i],matriz[i][N-i-1] = matriz[i][N-i-1],matriz[i][i]
    if i == 0:
        for j in range (int(N/2)):
            matriz[i][j],matriz[i][N-j-1] = matriz[i][N-j-1],matriz[i][j]
    
print(matriz)