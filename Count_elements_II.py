n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=set(a)
v=set(b)
k=list(k)
v=list(v)
c=0
for i in range (len(k)):
    
    if k[i] not in v:
        c+=1
for i in range (len(v)):
    if v[i] not in k:
        c+=1
print(c)