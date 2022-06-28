n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=0
min=0
s=0
for i in range(n):
    if a[i]>=b and a[i]<=c:
        d+=1
        print(a[i],end=' ')
if d==0:
    print(-1)
