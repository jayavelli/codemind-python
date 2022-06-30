n=int(input())
a=list(map(int,input().split()))
k,l=map(int,input().split())
s=[]
for i in range(n):
    if a[i]>=k and a[i]<=l:
        s.append(a[i])
if len(s)>0:
    print(min(s))
else:
    print(-1)