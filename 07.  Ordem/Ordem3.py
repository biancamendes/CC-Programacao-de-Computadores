N = int(input())
v_par = []
v_impar = []
   
for i in range (N):
    x = int(input())
    if x%2 == 0:
        v_par.append(x)
    else:
        v_impar.append(x)

for _ in v_par:
    for i in range (len(v_par)-1):
        if (v_par[i]>v_par[i+1]):
            v_par[i],v_par[i+1]=v_par[i+1],v_par[i]    

for _ in v_impar:
    for i in range (len(v_impar)-1):
        if (v_impar[i]<v_impar[i+1]):
            v_impar[i],v_impar[i+1]=v_impar[i+1],v_impar[i]

v = []
v.extend(v_par)
v.extend(v_impar)

print(v)