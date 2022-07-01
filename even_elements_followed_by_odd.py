n=int(input())
a=list(map(int,input().split()))

k=[]
s=0
max=0
for i in range(n):
    if a[i]%2==0:
        print(a[i],end=' ')
for i in range(n):
    if a[i]%2!=0:
        print(a[i],end=' ')