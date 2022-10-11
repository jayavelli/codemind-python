from itertools import permutations
a,b=map(int,input().split())
x=[]
x=list(permutations(range(1, a+1)))
c=list(x[b-1])
for i in c:
    print(i,end="")