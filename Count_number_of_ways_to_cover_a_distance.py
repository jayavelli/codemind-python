def dis(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return dis(n-1)+dis(n-2)+dis(n-3)
n=int(input())
k=dis(n)
print(k)