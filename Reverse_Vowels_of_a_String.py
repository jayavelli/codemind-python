def rev(s):
	v = ""
	for i in s:
		if i in "aeiouAEIOU":
			v+= i
	res=""
	for j in s:
		if j in "aeiouAEIOU":
			res += v[-1]
			v=v[:-1]
		else:
			res+= j
	return res
s=input()
print(rev(s))