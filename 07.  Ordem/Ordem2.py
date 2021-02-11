N = int(input())
v = []

for i in range (N):
    x = int(input())
    repeat = False    
    for i in v: 
        if x == i:
            repeat = True   
    if repeat == False:
        v.append(x)
    
for _ in v:
    for i in range (len(v)-1):
        if (v[i]>v[i+1]):
            v[i],v[i+1]=v[i+1],v[i]    
    
print(v)