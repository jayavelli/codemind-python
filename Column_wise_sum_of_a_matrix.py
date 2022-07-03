a,b=map(int,input().split())
l=[]
for i in range(a):
    k=list(map(int,input().split()))
    if len(k)==b:
        l.append(k)
        
e=0
o=0
for j in range(b):
    for i in range(a):
        e+=l[i][j]
    print(e,end=' ')
    e=0
    