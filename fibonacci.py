def fib(n):##5
    if(n<=1):
        return n
    return fib(n-1)+fib(n-2)
n=int(input())##7
for i in range(n):##
    print(fib(i),end=' ')

