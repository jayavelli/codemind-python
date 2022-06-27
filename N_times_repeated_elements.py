n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
for i in range(n):
    if a.count(a[i])==k and a[i] not in b:
        b.append(a[i])
if len(b)==0:
    print(-1)
else:
    print(*b)