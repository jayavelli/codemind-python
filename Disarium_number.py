import math
n=int(input())
t=n
res=0
d=int(math.log10(n)+1)
while(t!=0):
    r=t%10
    res=res+r**d
    t//=10
    d-=1
if(res==n):
    print("True")
else:
    print("False")
