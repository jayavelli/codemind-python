s=input()
k='aeiou'
a=[]
c=0
for i in s:
    if i in k and i not in a:
        a.append(i)
for i in k:
    if i not in a:
        c+=1
        print(i,end=' ')
if c==0:
    print(0)
        