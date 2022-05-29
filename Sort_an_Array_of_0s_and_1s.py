n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(0,n):
    if(a[i]==0):
        b.append(a[i])
    elif(a[i]!=0):
        c.append(a[i])
print(*(b+c))
        