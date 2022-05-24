n=int(input())
fact=1
for i in range(1,n+1):
    fact=1
    n=int(input())
    for j in range(1,n+1):
        fact=fact*j
    print(fact)