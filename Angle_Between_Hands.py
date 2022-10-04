s=input()
h=((ord(s[0])-48)*10+ord(s[1])-48)
m=((ord(s[3])-48)*10+ord(s[4])-48)
a=(11/2)*m-30*h
if a<0:
    a+=360
if a>180:
    a=360-a
print("{:.1f}".format(a))