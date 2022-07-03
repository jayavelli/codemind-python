p=input()
n=p.lower()

k=''
for i in n:
    if i not in k and ord(i)!=32:
        k+=i
s=list(k)
s.sort()
print(len(s))
    