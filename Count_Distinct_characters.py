p=input()
p=p.lower()
p=p.split()
p=''.join(p)
p=sorted(p)
p=set(p)
print(len(p))