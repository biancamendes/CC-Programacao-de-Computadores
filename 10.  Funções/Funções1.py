def maiorGranizo(h0):
    maior = h0
    
    while h0 != 1:    
          
        if h0%2 == 0:
            h1 = h0/2
        else:
            h1 = 3*h0+1
            
        h0 = h1
        
        if h0 > maior:
            maior = h0    
    
    return maior

h0 = int(input())
maior = maiorGranizo(h0)
print(int(maior))