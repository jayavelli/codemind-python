n=int(input())
a=list(map(int,input().split()))
c=0
s=0
if n%2!=0:
    a.append(0)
print(*a)