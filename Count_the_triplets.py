n=int(input())
a=[]
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    s=len(l)
    t=0
    c=0
    b=[]
    d=0
    for i in range(0,s-1):
        for j in range(i+1,s):
            d=l[i]+l[j]
            for k in range(j+1,len(l)):
                if d==l[k]:
                    c+=1
                    b.append(c)
                    t=0
    if c>0:
        print(c)
    else:
        print(-1)