n=int(input())
a=list(map(int,input().split()))
c=0
c2=0
for i in range(n-1,-1,-1):
    if a[i]%2==0:
        print(a[i])
        break