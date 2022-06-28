
n,m=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=list(a)+list(b)
k=[]
for i in range(len(c)):
    if i not in k and c.count(i)>1 :
        k.append(i)

print(len(k))
    