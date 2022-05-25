n=int(input())
a=list(map(int,input().split()))
c=0
f=0
for i in a:
    if(i%2==0):
        c+=1
    else:
        f+=1
print(c,f)
    
