n=int(input())
k = n-1
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k-=1
    for j in range(1, i+2):
     
        # printing stars
        print(j, end="")
    for j in range(i,0,-1):
        print(j, end="")
    print()