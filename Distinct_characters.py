p=input()
s=p.lower()
k=[]
l=[]
a='abcdefghijklmnopqrstuvwxyz'
for i in s:
   if s.count(i)==1:
        k.append(i)
        
for i in a:
    if i in k:
        l.append(i)
m=''.join(l)
print(m)
        
