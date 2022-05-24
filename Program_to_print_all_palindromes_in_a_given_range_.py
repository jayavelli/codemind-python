a=int(input())
b=int(input())
for i in range(a,b+1):
    var=i
    sum=0
    while var>0:
        r=var%10
        sum=sum*10+r
        var=var//10
    if(sum==i):
        print(i,end=" ")
