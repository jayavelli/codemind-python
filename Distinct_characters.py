p=input()
n=p.lower()

k=''
for i in n:
    if i not in k and ord(i)!=32:
        k+=i
s=list(k)
s.sort()
for i in s:
    print(i,end='')
    