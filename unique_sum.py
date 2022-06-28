n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(n):
    c=1
    for j in range(n):
        if a[i]!=-1:
            if a[i]==a[j] and i!=j:
                c+=1
                a[i]=-1
    if c==1:
        s+=a[i]
print(s)