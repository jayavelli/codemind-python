n=int(input())
m=int(input())
k=[]
s=0
for i in range(n):
    r=list(map(int,input().split()))
    for j in range(m):
        k.append(r)
        break
for i in range(n):
    for j in range(m):
        s+=k[i][j]
print(s)
    