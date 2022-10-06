n=input()
n=n.lower()
n=n.split()
k=[]
a=["a","e","i","o","u"]
for i in n:
    c=0
    for j in i:
        if j in a:
            c+=1
    k.append(c)
print(max(k))