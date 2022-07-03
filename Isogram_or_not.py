v=input()

k=''
c=0
for i in v:
    if i not in k:
        k+=i
if len(v)==len(k):
    print(True)
else:
    print(False)