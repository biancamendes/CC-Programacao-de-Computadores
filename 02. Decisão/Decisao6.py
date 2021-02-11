import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

a = math.sqrt((x1-x2)**2+(y1-y2)**2)
b = math.sqrt((x1-x3)**2+(y1-y3)**2)
c = math.sqrt((x2-x3)**2+(y2-y3)**2)

if (math.fabs(b-c)<a<(b+c)) and (math.fabs(a-c)<b<(a+c)) and (math.fabs(a-b)<c<(a+b)):
    if (a==b) and (a==c):
        print('equilátero')
    else:
        if (a==b) or (a==c) or (b==c):
            print('isósceles')
        else:
            print('escaleno')
else:
    print('inexistente')
        