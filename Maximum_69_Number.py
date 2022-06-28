n=int(input())
k=0
for i in str(n):
    if k==0:
        if i=='6':
            i='9'
            k=1
    print(i,end='')