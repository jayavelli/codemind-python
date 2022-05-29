n=int(input())
k=n*n
s=0
while(k!=0):
    r=k%10
    s+=r
    k//=10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")