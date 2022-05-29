n=int(input())
m=int(input())
s=0
k=0
for i in range(1,n):
    if(n%i==0):
        s+=i#284
for j in range(1,m):
    if(m%j==0):
        k+=j#220
if(s==m and k==n):
    print("Amicable")
else:
    print("Not Amicable")
