n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    p=a[i]
    while p:
        r=p%10
        p//=10
        s+=r
print(s)
        