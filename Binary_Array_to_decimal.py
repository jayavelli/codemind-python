n=int(input())
a=list(map(int,input().split()))

k=0
s=0
max=0
for i in range(n):
    k+=(2**s)*a[n-1-i]
    s+=1
print(k)