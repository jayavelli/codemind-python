n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
t=c=0
ind=0
for i in range(n):
    t=a.count(a[i])
    if(t>c):
        c=t
        ind=i
m=a[ind]
print(m)