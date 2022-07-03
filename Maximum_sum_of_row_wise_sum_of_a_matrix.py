a,b=map(int,input().split())
l=[]
for i in range(a):
    k=list(map(int,input().split()))
    if len(k)==b:
        l.append(k)
        
e=0
o=0
for i in range(a):
    for j in range(b):
        e+=l[i][j]
    if o<e:
        o=e
    e=0
print(o)
    