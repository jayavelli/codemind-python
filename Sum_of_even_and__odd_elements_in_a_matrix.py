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
        if l[i][j]%2==0:
            e+=l[i][j]
        else:
            o+=l[i][j]
print(e,o)