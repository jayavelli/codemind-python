n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    k=str(a[i])
    m=k[::-1]
    if m==k:
        c+=1
print(c)
    