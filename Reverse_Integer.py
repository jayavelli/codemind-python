n=int(input())
k=abs(n)
s=0
while k!=0:
    
    r=k%10
    s=s*10+r
    k//=10
if n>0:
    print(s)
else:
    print(-s)