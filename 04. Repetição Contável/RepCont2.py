N = int(input())

x = int(input())    
soma = prod = menor = maior = x

for _ in range (N-1):
    
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