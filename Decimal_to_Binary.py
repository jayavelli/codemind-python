def bin(n):
    
    s=[]
    while n:
        r=n%2
        s.append(r)
        n//=2

    return s
a=int(input())
for i in range(a):
    j=int(input())
    k=bin(j)
    for i in k[::-1]:
        print(i,end="")
    print()