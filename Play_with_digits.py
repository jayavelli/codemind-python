n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    k=str(a[i])
    for j in k:
        s+=int(j)
print(s)