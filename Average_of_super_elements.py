n=int(input())
a=list(map(int,input().split()))
k=[]
c=0
for i in a:
    if i==a.count(i):
        k.append(i)
k=set(k)
for i in k:
    c+=i
if c>0:
    r=c/len(k)
    print("%.2f"%r)
else:
    print(-1)
    