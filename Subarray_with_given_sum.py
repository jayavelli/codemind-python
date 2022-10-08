n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    k=m=c=0
    for i in range(a):
        s=0
        for j in range(i,a):
            s+=l[j]
            if(s==b):
                k=i
                m=j
                c=1
                break
        if(c==1):
            break
    if(c==1):
        print(k+1,end=" ")
        print(m+1)
    else:
        print(-1)