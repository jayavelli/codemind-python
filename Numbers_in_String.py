a= input()

s= 0
for i in a:
    
    if ord(i) >= 48 and ord(i) <= 57:
    
        s+= int(i)
print(s)