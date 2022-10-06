n=input()
n=n.split()
n="".join(n)
n=n.lower()
k=[]
c=0
a=["a","e","i","o","u"]
for i in n:
    
    if n.count(i)==1:
        c+=1
print(c)