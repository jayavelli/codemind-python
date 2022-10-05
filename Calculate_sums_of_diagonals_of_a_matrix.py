n=int(input())
m=[]
s=0
d=0
for i in range(n):
    a=list(map(int,input().split()))
    m.append(a)
for i in range(n):
    for j in range(n):
        if i==j:
            s+=m[i][j]
        if i+j==n-1:
            d+=m[i][j]
print("Principal Diagonal:",s,sep="")
print("Secondary Diagonal:",d,sep="")