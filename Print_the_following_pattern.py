n=int(input())
for i in reversed(range(1,n+1)):
    for j in reversed(range(1,n+1)):
        if i==j or i+j==n+1:
            print(i,end=" ")
        else:
            print(" ",end="")
    print()