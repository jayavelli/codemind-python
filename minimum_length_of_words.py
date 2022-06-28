n=input()
s=n.split()
c=0
min=999
for i in s:
    c=len(i)
    if c<min:
        min=c
print(min)