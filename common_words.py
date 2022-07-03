p=input()
q=input()
p=p.lower()
q=q.lower()
s1=p.split()
s2=q.split()
k=[]
for i in s2:
    if i in s1:
        k.append(i)
print(*k)