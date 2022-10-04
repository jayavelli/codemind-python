def str(n):
    i=0
    s=0
    while n:
        r=n%10
        s+=2**i*r
        n//=10
        i+=1
    return s
a=int(input())
for i in range(a):
    j=int(input())
    print(str(j))