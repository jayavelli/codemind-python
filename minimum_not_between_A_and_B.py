n=int(input())
a=list(map(int,input().split()))
l,m=map(int,input().split())
c=0
k=[]
s=0
min=999
for i in range(n):
    if a[i]<l or a[i]>m:
        c+=1
        if a[i]<min:
            min=a[i]
if c==0:
    print(-1)
else:
    print(min)