a=int(input())

m=list(map(int,input().split()))
n=int(input())
c=0
b=[]
for i in range(n):
        m.insert(0,m[-1])
        m.pop()
print(*m)