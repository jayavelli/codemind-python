n=int(input())
pro=1
s=0
while(n!=0):
    r=n%10
    s+=r
    pro*=r
    n//=10
if(s==pro):
    print("Spy Number")
else:
    print("Not Spy Number")