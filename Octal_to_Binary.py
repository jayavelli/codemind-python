def dec(a):
    s=0
    i=0
    while a:
        r=a%10
        s=s+r*8**i
        a//=10
        i+=1
    return s
def oc(a):
    k=""
    a=dec(a)
    while a:
        r=a%2
        if r>=0:
            k+=str(r)
        a//=2
    k=k[::-1]
    print(k)
n=int(input())
for i in range(n):
    a=int(input())
    oc(a)
        