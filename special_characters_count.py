s=input()
n=s.lower()
c1=0
c2=0
for i in n:
    if ord(i)>=97 and ord(i)<=122 or ord(i)==32:
        continue
    else:
        c2+=1
print(c2)