import math
t=int(input())
n=t
d=int(math.log10(n)+1)
res=0
while(n!=0):
    r=n%10
    res=res+r**d
    n//=10
    d-=1
if res==t:
    print("True")

else:
    print("False")