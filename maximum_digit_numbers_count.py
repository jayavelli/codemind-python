n=int(input())
a=list(map(int,input().split()))
s=0
min=0
c=0
for i in range(n):
    if len(str(a[i]))>min:
        min=len(str(a[i]))
for i in range(n):
    if len(str(a[i]))==min:
        print(a[i],end=' ')