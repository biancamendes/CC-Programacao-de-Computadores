vetor = []
soma = 0

for _ in range (5):
    num = float(input())
    vetor.append(num)
    soma += num
    
media = soma / 5
dist = soma

for i in range (5):
    if ((vetor[i]-media)**2 < dist**2):
        dist = vetor[i]-media
        min = vetor[i]

print ('%.2f'%min)