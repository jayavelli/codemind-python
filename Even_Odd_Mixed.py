n=int(input())
c=0
x=0
while n:
    r=n%10
    if(r%2==0):
        c=1
    elif(r%2==1):
        x=1
    n//=10

if(c==1 and x==1):
    print("Mixed")
elif(c==1):
    print("Even")
elif(x==1):
    print("Odd")