N = int(input())

matriz = []

soma_acima = 0
soma_total = 0

for i in range (N):
    l = []    
    
    for j in range (N):
        a = int(input())
        l.append(a)
        soma_total += a
        if j>i:
            soma_acima += a
        
    matriz.append(l)
    
media = soma_total / N**2 
cont = 0
    
for i in range (N):
    for j in range (N):
        if matriz[i][j] < media:
            cont += 1
    
print(soma_acima)
print(cont)