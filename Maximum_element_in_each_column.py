r,c=map(int,input().split())
l=[]
for i in range(r):
    a=list(map(int,input().split()))
    l.append(a)
for i in range(c):
    max=0
    for j in range(r):
        if(l[j][i]>max):
            max=l[j][i]
    print(max)