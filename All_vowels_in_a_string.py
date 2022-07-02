s=input()
k='aeiou'
a=[]
c=0
for i in s:
    if i in k and i not in a:
        a.append(i)
if len(a)==5:
    print(True)
else:
    print(False)