n=int(input())
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
q=0
k = n-1
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k-=1
    for j in range(0,i+1):
        print(s[j], end="")
        q+=1
    for j in range(i-1,-1,-1):
        print(s[j], end="")
        q-=1
    print()