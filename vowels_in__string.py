s=input()
k='aeiouAEIOU'
a=[]
for i in s:
    if i in k and i not in a:
        a.append(i)
if len(a)>0:
    print(*a)
else:
    print(-1)
        