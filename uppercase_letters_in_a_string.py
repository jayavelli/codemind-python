s=input()
n=s.lower()
c1=0
c2=0
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        
        c2+=1
print(c2)