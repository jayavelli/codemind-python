n=int(input())
res=0
for i in range(1,n+1):
    m=int(input())
    temp=m
    res=0
    while(m!=0):
        r=m%10
        res=res*10+r
        m//=10
    if(temp==res):
        print("True")
    else:
        print("False")
    
        