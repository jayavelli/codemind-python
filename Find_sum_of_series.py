n=int(input())
d=1
a=1
r=0
while n>0:
    r+=1/(a+(n-1)*d);
    n-=1
    
print("%.2f"%r)
    