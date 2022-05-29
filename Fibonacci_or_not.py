n=int(input())
a,b=0,1
k=0
for i in range(n+1):
    c=a+b
    if(c==n):
        k=1
    a=b
    b=c
if(k==1):
    print("True")
else:
    print("False")