n=int(input())
a=list(map(int,input().split()))
k=[]
c=0
s=0
for i in range(n):
    if a[i]!=-1:
         c=1
         for j in range(n):
             if a[i]==a[j] and i!=j:
                 c+=1
                 a[j]=-1
    if a[i]==c:
        k.append(a[i])
for i in range(len(k)):
    s+=k[i]
if len(k)==0:
    print(-1)
else:
    avg=s/len(k)
    print("{:.2f}".format(avg))