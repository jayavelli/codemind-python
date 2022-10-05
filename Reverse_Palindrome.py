def rev(n):
    re=0
    t=n
    while(t):
        r=t%10
        re=re*10+r
        t//=10
    return re
def palind(n):
    re=0
    t=n
    k=0
    while(t):
        r=t%10
        re=re*10+r
        t//=10
    if n==re:
        return True
    elif n!=re:
        return False
        return palind(n+re)
n=int(input())
k=n
s=0
while(True):
    if(palind(k+rev(k))):
        print(k+rev(k))
        break
    k+=rev(k)