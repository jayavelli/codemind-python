n=int(input())
a=list(map(int,input().split()))
l,m=map(int,input().split())
c=0
k=[]
s=0
max=0
for i in range(n):
    if a[i]<l or  a[i]>m:
        c+=a[i]
    

print(c)