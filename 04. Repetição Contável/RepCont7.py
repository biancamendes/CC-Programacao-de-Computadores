X = int(input())

for i in range (0,X):
    
    if i == 0:
        x0 = 0
        print(x0)
    else:    
        if i == 1:
            x1 = 1
            print(x1)
        else:
            x2 = x0+x1
            x0 = x1
            x1 = x2
            print(x2)