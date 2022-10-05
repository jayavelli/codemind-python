n=int(input())
k=[]
c=0
for i in range(n):
    
    a=int(input())
    k.append(a)
m=int(input())
for i in range(len(k)):
    if(k[i]<=m):
        c+=1
    elif(k[i]>m):
        c+=2
print(c)
    