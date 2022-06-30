n=int(input())
a=list(map(int,input().split()))
c=0
min=9999
for i in range(n):
    if len(str(a[i]))<min:
        min=len(str(a[i]))
for i in range(n):
    if len(str(a[i]))==min:
        c+=1
print(c)