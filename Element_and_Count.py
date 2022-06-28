n=int(input())
a=list(map(int,input().split()))
k=[]
p=[]
for i in range(n):
    if a[i] not in k:
        k.append(a[i])
        p.append(a.count(a[i]))
for i in range(len(k)):
    print(k[i],p[i],end=' ')