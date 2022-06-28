n=int(input())
a=list(map(int,input().split()))

d=0
min=999
for i in range(n):
    if a[i]%2==0:
        break
    d+=a[i]
print(d)
        