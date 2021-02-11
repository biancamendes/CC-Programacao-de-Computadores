n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1+n2 == n3) or (n1+n3 == n2) or (n2+n3 == n1):
    print ('soma')
else:
    if (n1*n2 == n3) or (n1*n3 == n2) or (n2*n3 == n1):
        print ('multi')
    else:
        if ((n1+n2+n3)%2 == 0):
            print ('par')
        else:
            print ('ímpar')