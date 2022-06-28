n,k=map(int,input().split())
a=list(map(int,input().split()))
s=0
min=0
c=0
for i in range(n):
    l=abs(a[i])
    if len(str(l))==k:
        c+=1
print(c)