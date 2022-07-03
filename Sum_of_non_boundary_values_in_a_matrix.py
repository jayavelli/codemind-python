a,b=map(int,input().split())
l=[]
for i in range(a):
    k=list(map(int,input().split()))
    if len(k)==b:
        l.append(k)
        
e=0
o=0
for i in range(1,a-1):
    for j in range(1,b-1):
        e+=l[i][j]
print(e)
    