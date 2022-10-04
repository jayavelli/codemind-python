a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    s=input()
    while(c):
        r=s[:c]
        s=r[::-1]+s[c:]
        c-=1
    print(s)