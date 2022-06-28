n=int(input())
a=list(map(int,input().split()))
k=[]
s=0
for i in range(n):
    if a[i]%2!=0:
        if a[i] not in k:
            k.append(a[i])
for i in range(len(k)):
    s+=k[i]
print(s)
            