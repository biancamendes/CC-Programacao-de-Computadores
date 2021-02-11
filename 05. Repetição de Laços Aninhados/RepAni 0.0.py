A = int(input())
B = int(input())

for i in range (A,B+1):
    primo = 0
    for j in range (2,int(i/2)+1):
        if (i%j == 0):
            primo = 1
            
    if primo == 0:
        print(i)        