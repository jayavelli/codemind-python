def hcf(a,b):
    hcf=0
    for i in range(1,b):
        if(a%i==0 and b%i==0):
            hcf=i
    return hcf
a,b=map(int,input().split())
print(hcf(a,b))

        
