n=int(input())
a=list(map(int,input().split()))
l=a[0]
h=a[n-1]
f=0
for i in range(0,n):
    m=(l+h)//2
    if(a[i]==m):
        f=1
        break
    else:
        f=0
if(f==1):
    print("True")
else:
    print("False")
