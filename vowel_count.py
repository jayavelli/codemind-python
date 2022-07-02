s=input()
k='aeiouAEIOU'
a=[]
c=0
for i in s:
    if i in k:
        c+=1
print(c)
