n=int(input())
while n>10:
    s=0
    for i in str(n):
        s+=int(i)
    n=s
print(s)
    