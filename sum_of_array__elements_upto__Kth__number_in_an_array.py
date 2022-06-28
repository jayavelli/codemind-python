n=int(input())
a=list(map(int,input().split()))
b=int(input())
d=0
min=999
for i in range(n):
    if a[i]<=b:
        d+=a[i]
print(d)
        