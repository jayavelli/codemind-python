s=input()
n=s.lower()
c1=0
c2=0
for i in n:
    if ord(i)==32:
        
        c2+=1
print(c2)