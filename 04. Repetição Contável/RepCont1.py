N = int(input())

soma  = 0
prod  = 1
menor = 100
maior = 0

for _ in range (N):
    
    x = int(input())
    
    soma += x
    prod *= x    
    
    if x < (menor):
        menor = x
    if x > (maior):
        maior = x

print ('%.2f'%(soma/N))
print (soma)
print (prod)
print (menor)
print (maior)