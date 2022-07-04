p=input()
p=p.lower()
p=p.split()
p=''.join(p)
c=0
for i in p:
    if p.count(i)==1:
        c=i
        break
if c==0:
    print(-1)
else:
    print(c)