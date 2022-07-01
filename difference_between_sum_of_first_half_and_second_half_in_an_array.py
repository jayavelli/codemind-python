n=int(input())
a=list(map(int,input().split()))
s=0
s2=0
for i in range(n//2):
    s+=a[i]
for i in range(n//2,n):
    s2+=a[i]
    
k=abs(s2-s)
print(k)
