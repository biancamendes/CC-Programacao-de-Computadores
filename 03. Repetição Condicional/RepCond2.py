alunos = int(input())
i=1
soma = 0

while i <= alunos:
    n1 = float(input())
    n2 = float(input())
    media = (n1+n2)/2
    soma += media
    i += 1

print('%.2f'%(soma))