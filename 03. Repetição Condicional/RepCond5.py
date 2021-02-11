N = int(input())
n1 = int(input())
cond = 'sim'
i = 1

while i < N:
    n2 = int(input())
    if (n2 < n1):
        cond = 'não'
    n1 = n2
    i += 1

print(cond)