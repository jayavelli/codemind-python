n=int(input())
v="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    for j in range(i,n):
        print(v[n-i-1],end=" ")
    print()