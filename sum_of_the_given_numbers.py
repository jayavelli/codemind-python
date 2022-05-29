n=int(input())
s=0
for i in range(1,n+1):
    m,c=list(map(int,input().split()))
    s=m+c
    print(s)