n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    s=0
    for j in range(i,m+1):
        s+=j
        if s%2==1:
            c+=1
print(c)