N = int(input())

for _ in range (N):
    v = [0]*5
    cont = 0
    
    for i in range (5):
        v[i] = int(input())
    
    for i in range (5):
        for j in range (4):
            if (v[j]>v[j+1]):
                v[j],v[j+1]=v[j+1],v[j]    
                cont += 1
    
    print(cont)