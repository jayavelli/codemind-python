n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
min=0
for i in range(n):
    k=abs(a[i])
    if len(str(k))==m:
        c+=1
print(c)