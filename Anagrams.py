v=input()
m=input()
s=v.lower()
n=m.lower()
c=0
for i in s:
   if i in n:
       c+=1
if c==len(s)==len(n):
    print(True)
else:
    print(False)