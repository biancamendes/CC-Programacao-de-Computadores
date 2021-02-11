vetor = []

for _ in range (10):
    vetor.append(int(input()))
    
n = int(input())
pos = []

for i in range (10):
    if vetor[i] == n:
        pos.append(i)

print(pos)