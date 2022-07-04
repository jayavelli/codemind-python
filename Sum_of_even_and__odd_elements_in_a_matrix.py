a,b=map(int,input().split())
s=0
k=[]
o=0
max=0
for i in range(a):
    n=list(map(int,input().split()))
    if len(n)==b:
        k.append(n)
for i in range(a):
    for j in range(b):
        if k[i][j]%2==0:
            s+=k[i][j]
        else:
            o+=k[i][j]
print(s,o)
        