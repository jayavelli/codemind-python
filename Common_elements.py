n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=[]
for i in a:
    if i not in k and i in b:
        k.append(i)
print(*k)