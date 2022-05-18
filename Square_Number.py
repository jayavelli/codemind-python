n=int(input())
for i in range(int(n/2)+1):
    if(n==i*i):
        print("True")
        break
else:
    print("False")