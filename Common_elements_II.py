
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

k=[]
for i in range(n):
    if a[i] not in b  :
        k.append(a[i])
for i in range(m):
    if b[i] not in a:
        k.append(b[i])
print(*k)
    