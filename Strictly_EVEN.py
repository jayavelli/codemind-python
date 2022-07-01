n=int(input())
a=list(map(int,input().split()))
c=0
c2=0
for i in range(n):
    if a[i]%2==0 and i%2==0:
        c+=1
for i in range(n):
    if i%2!=0 and a[i]%2==0:
        c2+=1
if c2>0:
    print(False)
else:
    print(True)