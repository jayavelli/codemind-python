n=int(input())
a=list(map(int,input().split()))

k=[]
s=0
max=0
for i in range(n):
    if a[i]%2==0:
        s+=1
if s==n:
    print("True")
else:
    print("False")