a,b=map(int,input().split())
s=0
k=[]
for i in range(a):
    n=list(map(int,input().split()))
    if len(n)==b:
        k.append(n)
for i in range(1,a-1):
    for j in range(1,b-1):
        s+=k[i][j]
print(s)
    