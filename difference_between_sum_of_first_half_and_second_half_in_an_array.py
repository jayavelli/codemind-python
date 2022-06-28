n=int(input())
a=list(map(int,input().split()))
k=n//2
d=0
s=0
min=999
for i in range(k):
    d+=a[i]
for i in range(k,n):
    s+=a[i]
print(abs(d-s))