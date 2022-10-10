n=int(input())
k=n
a=n+(n-1)
for i in range(a):
    for j in range(a):
        if i<=n-1:
            if i==0:
                print(k,end=" ")
            if i>=1:
                if j<i:
                    print(k-j,end=" ")
                elif j>=i and j<a-i:
                    print(k-i,end=" ")
                else:
                    print((j-k+1)+1,end=" ")
        elif i==n-1:
            if j<n:
                print(k-j,end=" ")
            else:
                print((j-k+1)+1,end=" ")
        elif i>=n:
            x=a-i-1
            if i==a:
                print(k,end=" ")
            if j<x:
                print(k-j,end=" ")
            elif j>=x and j<a-x:
                print(k-x,end=" ")
            else:
                print((j-k+1)+1,end=" ")
    print()