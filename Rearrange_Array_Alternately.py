a=int(input())


b=[]
for i in range(a):
    n=int(input())
    m=list(map(int,input().split()))
    k=n//2
    if(n%2==0):
        for i in range(n//2):
            if(i<k-1):
                print(m[n-1-i],m[i],end=" ")
            else:
                print(m[n-1-i],m[i],end="")

    else:
        for i in range(n//2):
            print(m[n-1-i],m[i],end=" ")
        print(m[k],end="")
    print()