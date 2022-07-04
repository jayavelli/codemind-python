a,b=map(int,input().split())
s=0
k=[]
for i in range(a):
    n=list(map(int,input().split()))
    if len(n)==b:
        k.append(n)
for i in range(a):
    for j in range(b):
       if i==0 or i==a-1 or j==0 or j==b-1:
           s+=k[i][j]
print(s)