def prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n=int(input())
l=len(str(n))
c=0
if prime(n):
    for j in str(n):
        if prime(int(j)):
            c+=1
if c==l:
    print("Mega Prime")
else:
    print("Not Mega Prime")