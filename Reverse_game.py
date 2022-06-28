def rev(n):
    p=n
    r=0
    while n:
        k=n%10
        r=r*10+k
        n//=10
    return r

n=int(input())
a=list(map(int,input().split()))
c=0
k=[]
for i in range(n):
    k.append(rev(a[i]))
for i in range(n):
    print(k[i],end=' ')
    