n=int(input())
a=list(map(int,input().split()))
x=int(input())
f=0
for i in range(0,n):
    if(a[i]==x):
        f=1
if(f==1):
    print("True")
else:
    print("False")