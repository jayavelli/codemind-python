def prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n=int(input())
i=n
k=n
c1=0
c2=0
if prime(n):
    print(0)
else:
     
    while 1:
        if prime(i):
            z=i
            break
        i+=1
        c1+=1
    while 1:
        if prime(k):
            v=k
            break
        k-=1
        c2+=1
    if c1>=c2:
        print(c2)
    else:
       print(c1)