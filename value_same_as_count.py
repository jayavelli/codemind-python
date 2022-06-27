n=int(input())
a=list(map(int,input().split()))
k=[]
s=0
c=0
p=0
for i in range(n):
    if a[i]!=-1:
        c=1
        for j in range(n):
            if a[i]==a[j] and i!=j:
                c+=1
                a[j]=-1
        if a[i]==c:
            k.append(a[i])
for i in range(len(k)):
    p+=1
print(p)