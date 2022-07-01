n=int(input())
a=list(map(int,input().split()))

k=[]
s=0
max=0
for i in range(n):
    s+=a[i]
av=s//n
for i in range(n):
    if a[i]>=av:
        max+=1
print(max)