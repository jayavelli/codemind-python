a=int(input())

m=list(map(int,input().split()))

b=[]
for i in range(a):
    c=0
    f=0
    for j in range(i+1,a):
        if(m[j]>m[i]):
            print(c+1,end=" ")
            f=1
            break
        else:
            c+=1
    if(f==0):
        
        print("0",end=" ")
    
        