p=input()
for i in p:
    if p.count(i)==1:
        print(i)
        break
else:
    print(-1)