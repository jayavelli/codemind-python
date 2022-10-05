n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    s=(s*10)+a[i]
s+=1
arr=[]
while s>0:
    r=s%10
    arr.append(r)
    s//=10
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")