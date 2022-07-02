s=input()
n=s.split()
s=0
c=0
for i in n:
    print(abs(ord(min(i))-ord(max(i))),end=' ')