N = int(input())
matr = [0]*N
nota = [0]*N

for i in range (N):
    matr[i] = int(input())
    
for i in range (N):
    nota[i] = float(input())
      
for _ in range (N):
    for i in range (N-1):
        if (nota[i]>nota[i+1]):
            nota[i],nota[i+1]=nota[i+1],nota[i]    
            matr[i],matr[i+1]=matr[i+1],matr[i]   
    
print(matr)