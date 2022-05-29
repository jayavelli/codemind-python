n=int(input())
temp=n
fact=1
s=0
while(n!=0):
    r=n%10
    fact=1
    for i in range(1,r+1):
        fact*=i
    s+=fact
    n//=10

if(s==temp):
    print("The number", temp ,"is a strong number")
else:
    print("The number",temp,"is not a strong number")