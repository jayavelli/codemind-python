n,m=map(int,input().split())
a=[]
for i in range(n):
    s=0
    r=list(map(int,input().split()))
    for k in r:
        s+=k
    for j in range(m):
        a.append(s)
        break
print(max(a))