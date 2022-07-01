n=int(input())
a=list(map(int,input().split()))
l=int(input())
c=0
k=[]
s=0
for i in range(n):
    if a.count(a[i])==l and a[i] not in k:
        k.append(a[i])
if len(k)==0:
    print(-1)
else:
    print(*k)