n=int(input())
s=n*n
k=0
while(s!=0):
    r=s%10
    s//=10
    k+=r
if k==n:
    print("Neon Number")
else:
    print("Not Neon Number")