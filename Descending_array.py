n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n-1):
    if a[i]>a[i+1]:
        s+=1
if s+1==n:
    print("yes")
else:
    print("no")