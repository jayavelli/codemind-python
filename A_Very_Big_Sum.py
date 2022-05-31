a=int(input())
n=list(map(int,input().split()))
c=0
for i in range(0,a):
    c+=n[i]
print(c)