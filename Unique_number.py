k=int(input())
c=0
v=0

for i in range(1,10):
    n=k
    c=0
    while(n!=0):
        r=n%10
        if(r==i):
            c+=1
        n//=10
    if(c>1):
        v+=1
if(v==0):
    print("Unique Number")
else:
    print("Not Unique Number")
        
    
            