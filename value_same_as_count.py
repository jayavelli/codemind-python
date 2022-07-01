n=int(input())
a=list(map(int,input().split()))
c=0
k=[]
s=0
for i in range(n):
    if a[i]!=-1:
        c=1
        for j in range (n):
            if a[i]==a[j] and i!=j:
                c+=1
                a[j]=-1
                
        if a[i]==c:
            s+=1
print(s)