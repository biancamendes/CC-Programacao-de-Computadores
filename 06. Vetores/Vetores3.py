N = int(input())
A = []
Ainv = []
B = []

for i in range (N):
    x = int(input())
    A.append(x)
    Ainv = [x] + Ainv
    
for i in range (N):
    if (Ainv[i] >= 0):
        fat = 1
        for j in range (1,Ainv[i]+1):
            fat *= j
        B.append(fat)
    else:
        B.append(Ainv[i])

print(B)