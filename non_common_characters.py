n=input()
p=input()
n=n.split()
n="".join(n)
n=n.lower()
p=p.split()
p="".join(p)
p=p.lower()
s=n+p
s=sorted(set(s))
for i in s:
    if i not in n:
        print(i,end="")
    elif i not in p:
        print(i,end="")