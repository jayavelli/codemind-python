v=input()
s=v.lower()
n=s.split()
c=0
for i in n:
    p=i
    k=i[::-1]
    if p==k:
        c+=1
print(c)
        