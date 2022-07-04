p=input()
p=p.lower()
p=p.split()
p=''.join(p)
p=sorted(p)
for i in p:
    if p.count(i)==1:
        print(i,end='')