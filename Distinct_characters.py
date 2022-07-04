p=input()
p=p.lower()
p=p.split()
p=''.join(p)
p=set(p)
p=sorted(p)
for i in p:

        print(i,end='')