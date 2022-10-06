def bi(n):
    s=""
    while n:
        r=n%2
        s+=str(r)
        n//=2
    return s
def com(n):
    n=bi(n)
    s=''
    for i in n:
        if i=='1':
            s+='0'
        elif i=='0':
            s+='1'
    s=s[::-1]
    k=0
    i=0
    s=int(s)
    while s:
        r=s%10
        k+=r*2**i
        s//=10
        i+=1
    print(k)
n=int(input())
com(n)
