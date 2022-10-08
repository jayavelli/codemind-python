a=int(input())
for i in range(a):
    n=int(input())
    m=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(m[i]%2!=0):
            c+=1
    print(c//2)