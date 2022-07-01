n=int(input())
a=list(map(int,input().split()))
c=0
k=[]
s=0
for i in range(n):
    if a[i] not in k:
        k.append(a[i])
print(*k)