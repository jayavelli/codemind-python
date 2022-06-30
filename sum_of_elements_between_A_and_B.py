n=int(input())
a=list(map(int,input().split()))
k,l=map(int,input().split())
s=0
for i in range(n):
    if a[i]>=k and a[i]<=l:
        s+=a[i]
print(s)