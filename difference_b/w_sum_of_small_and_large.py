s=input()
n=s.split()
s=0
c=0
for i in n:
    s+=ord(min(i))
    c+=ord(max(i))
print(c-s)