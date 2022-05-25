n=int(input())
m=int(input())
c=0
f=0
for i in range(n,m+1):
    temp=i
    c=0
    f=0
    while temp!=0:
        r=temp%10
        c+=1
        if(r!=0):
            if(i%r==0):
                f+=1
        temp//=10
    if(c==f):
        print(i,end=" ")
        
        