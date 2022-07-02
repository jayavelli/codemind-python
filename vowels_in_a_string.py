s=input()
n=s.split()
l=len(n)
m=input()
p=0
k='aeiouAEIOU'
for i in str(s):
    if i==m:
        print(True)
        print(p)
      
        break
    p+=1
else:
    print(False)