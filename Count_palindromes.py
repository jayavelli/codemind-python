def rev(n):
    p=n
    r=0
    while n:
        k=n%10
        r=r*10+k
        n//=10
    if p==r:
        return True
    else:
        return False

n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if rev(a[i]):
        c+=1
print(c)
