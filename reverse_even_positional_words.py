s=input()
n=s.split()
l=len(n)
for i in range(l):
    if i%2==0:
        print(n[i][::-1],end=' ')
    else:
        print(n[i],end=' ')