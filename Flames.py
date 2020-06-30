def remchar(name1,name2):
	name3 = name1
	name4 = name2
	for x in range(len(name1)):
		for y in range(len(name2)):
			if name1[x] == name2[y]:
				ch = name1[x]
				name3 = name3.replace(ch,'')
				name4 = name4.replace(ch,'')
	return(name3,name4)




def flame(y):
	flames = ['Friend','Lover','Affection','Marriage','Enemies','Sibling']
	p = None
	k = list('012345')
	print(k)
	while len(k)>1:
		for i in range(y):
			if  p == None or p >= len(k) - 1:
				p = 0
				continue
			p += 1
		#print(p)
		k.remove(k[p])
		#print(k)
		if p == len(k) - 1 or p == 0:
				p = None
		else:
			p -= 1
		print(k)
	#print(int(k[0]))
	return(flames[int(k[0])])
			
			
		

name1 = input("Person 1 name:").upper()
name2 = input("Person 2 name:").upper()
#name1 = name1.upper()
x = remchar(name1,name2)
y = x[0] + x[1]
#print(name1,name2)
print(y)
z = flame(len(y))
print("The relation between ",name1," and ",name2," will end in ",z)