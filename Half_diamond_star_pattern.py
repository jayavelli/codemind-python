n=int(input())
c=1
if(n>=3):
    for i in range(1,n*2):
        for j in range(1,c+1):
            print("*",end="")
        if(i<n):
            c+=1
        else:
            c-=1
        print()
else:
    print("The pattern is not possible")