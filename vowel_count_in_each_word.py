s=input()
n=s.split()
l=len(n)
c=0
p=0
k='aeiou'
for i in n:
    for j in i:
        if j in k:
            c+=1
    print(c,end=' ')
    c=0