a,b=map(int,input().split())
s=0
k=[]
max=0
for i in range(a):
    n=list(map(int,input().split()))
    if len(n)==b:
        k.append(n)
for i in range(a):
    for j in range(b):
       s+=k[i][j]
    if s>max:
        max=s
    s=0
print(max)