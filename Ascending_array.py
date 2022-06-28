
n=int(input())
a=list(map(int,input().split()))
c=1
for i in range(n-1):
    if a[i]<a[i+1]:
        c+=1
    else:
        break
if c==n:
    print("yes")
else:
    print('no')