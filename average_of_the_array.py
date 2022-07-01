n=int(input())
a=list(map(int,input().split()))
c=0
s=0
avg=0
for i in range(n):
    s+=a[i]
avg=s/n
print("%.2f"%avg)