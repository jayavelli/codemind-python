def pal(n):
    k=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    if rev==k:
        return k
n=int(input())
k=n+1
v=n-1
c1=0
c2=0
while 1:
    if pal(k)==k:
        z=k
        break
    k+=1
    c1+=1
while 1:
    if pal(v)==v:
        l=v
        break
    v-=1
    c2+=1
if c1==c2:
    print(l,z)
elif c1<c2:
    print(z)
else:
    print(l)