N = int(input())
M = int(input())

matriz = []

for i in range (N):
    l = []       
    
    for j in range (M):
        a = int(input())
        l.append(a)    
        
    matriz.append(l)
    
    menor = []
    
for j in range (M):    
    a = ((matriz[0][j])**2)**(1/2)
    menor.append(a) 
    
    for i in range (1,N):
        a = ((matriz[i][j])**2)**(1/2)
        if a < menor[j]:
            menor[j] = a
        
    for i in range (N):
        matriz[i][j]+=menor[j]
        matriz[i][j]=int(matriz[i][j])
    
print(matriz)