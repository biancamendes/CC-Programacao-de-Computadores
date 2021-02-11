N = int(input())
M = int(input())
A = []
B = []
C = []

for _ in range (N):
    A.append(int(input()))
    
for _ in range (M):
    B.append(int(input()))
    
for i in range (N):
    C= C + [A[i]] + [B[i]]
    
if M > N:
    for i in range (N,M):
        C = C + [B[i]]

print(C)