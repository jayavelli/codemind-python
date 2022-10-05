n=int(input())
c=1
for i in range(n):
    a=int(input())
    k=list(map(int,input().split()))
    if k==sorted(k):
        c=0
    else:
        c=max(k)-min(k)
    print(c)
    