def prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n=int(input())
m=int(input())
k=n+m
c=1
while 1:
    if prime(k+c):
        print(c)
        break
    c+=1
