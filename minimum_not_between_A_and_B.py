n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=0
min=999
for i in range(n):
    if a[i]<b or a[i]>c:
        d+=1
        if a[i]<min:
            min=a[i]
if d==0:
    print(-1)
else:
    print(min)