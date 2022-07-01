n=int(input())
a=list(map(int,input().split()))
c=0
s=0
avg=0
for i in range(n):
    s+=a[i]
avg=s//n
for i in range(n):
    if avg==a[i]:
        print(True)
        break
else:
    print(False)
    