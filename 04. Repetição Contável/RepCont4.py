n = int(input())
x = 0

for i in range (int(n/2)):
    
    if (i*(i+1)*(i+2) == n):
        x=1
        print(i)
        print(i+1)
        print(i+2)

if x==0:
    print ("não")