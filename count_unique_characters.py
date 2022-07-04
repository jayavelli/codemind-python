p=input()
p=p.lower()
p=p.split()
p=''.join(p)
p=sorted(p)
c=0
for i in p:
    if p.count(i)==1:
        c+=1
print(c)