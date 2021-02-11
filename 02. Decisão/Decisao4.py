n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1 == n2) and (n1 == n3):
    print (0)
else:
    if (n1 == n2):
        print (n3)
    else:
        if (n1 == n3):
            print (n2)
        else:
            if (n2 == n3):
                print (n1)
            else:
                print (n1+n2+n3)
