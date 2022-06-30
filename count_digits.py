n=int(input())
a=list(map(int,input().split()))
c=0
min=0
for i in range(n):
    k=str(abs(a[i]))
    print(len(k),end=' ')