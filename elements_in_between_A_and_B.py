n=int(input())
a=list(map(int,input().split()))
k,l=map(int,input().split())
s=[]
for i in a:
    if i>=k and i<=l:
        s.append(i)
if len(s)>0:
    print(*s)
else:
    print(-1)