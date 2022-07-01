n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if a[i]==k:
        c+=1
        break
if c>0:
    print(True)
else:
    print(False)
        