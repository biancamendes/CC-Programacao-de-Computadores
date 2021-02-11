x  = 3
i  = 1

vj1 = 0
vj2 = 0
emp = 0

while i <= x:
    
    j1 = int(input())
    j2 = int(input())
    
    if (j1 == j2):
        emp += 1
    else:    
        #regras do jogo: 0-pedra 1-spock 2-paper 3-lagarto 4-tesoura
        if (j1 == 0):
            if (j2==1):
                vj2 += 1
            if (j2==2):
                vj2 += 1
            if (j2==3):
                vj1 += 1
            if (j2==4):
                vj1 += 1
        if (j1 == 1):
            if (j2==0):
                vj1 += 1
            if (j2==2):
                vj2 += 1
            if (j2==3):
                vj2 += 1
            if (j2==4):
                vj1 += 1
        if (j1 == 2):
            if (j2==0):
                vj1 += 1
            if (j2==1):
                vj1 += 1
            if (j2==3):
                vj2 += 1
            if (j2==4):
                vj2 += 1
        if (j1 == 3):
            if (j2==0):
                vj2 += 1
            if (j2==1):
                vj1 += 1
            if (j2==2):
                vj1 += 1
            if (j2==4):
                vj2 += 1
        if (j1 == 4):
            if (j2==0):
                vj2 += 1
            if (j2==1):
                vj2 += 1
            if (j2==2):
                vj1 += 1
            if (j2==3):
                vj1 += 1
                
    i +=1

print(vj1)
print(vj2)
print(emp)    