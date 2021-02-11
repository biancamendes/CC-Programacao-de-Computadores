def maiorSequenciaDecrescente(v):
    
    sequencias = []
    cont = 1
    
    for i in range (N-1):
        if v[i] > v[i+1]:
            cont += 1
            if i == N-2:
                sequencias.append(cont)
        else:
            sequencias.append(cont)
            cont = 1
            
    maior = 0
    
    for sequencia in sequencias:
        if sequencia > maior:
            maior = sequencia
    
    return maior

N = int(input())
v = [0]*N
for i in range (N):
    v[i] = int(input())

maior = maiorSequenciaDecrescente(v)

print(int(maior))
    