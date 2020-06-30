import math as m

n = int(input("Enter the size of the grid:"))
print("Rules for entering elements:".capitalize())
print("\t1: First element should be 0")
print("\t2: Enter the elements row-wise")
print("\t3: Number of elements in row should be of previously defined size\n\n")
c=[]
for i in range(n):
	b = []
	a = input().split()
	for j in a:
		if j != ' ':
			b.append(int(j))
	#print(b)
	c.append(b)
print("\n\n\n\n")
for i in c:
	for j in i:
		print(j,end=" ")
	print()
print("\n\n\n\n")


#0 3 6 9
#1 4 4 5
#8 2 5 4
#1 8 5 9


i = 0
j = 0
score = 0
while i <= n-1 and j <= n-1:
	if i == n-1 and j == n-1:
		break
	if i == n-1:
#		break
		score = m.floor(score/2) + c[i][j+1]
		j = j+1
		print("i=",i,"  j=",j)
		print(c[i][j],score)
	elif j == n-1:
		score =m.floor(score/2) + c[i+1][j]
		i = i+1
		print("i=",i,"  j=",j)
		print(c[i][j],score)	
	elif c[i][j+1] < c[i+1][j]:
		score = m.floor(score/2) + c[i][j+1]
		j = j+1
		print("i=",i,"  j=",j)
		print(c[i][j],score)
	else:
		score =m.floor(score/2) + c[i+1][j]
		i = i+1
		print("i=",i,"  j=",j)
		print(c[i][j],score)

print("\n\n\n\n")				
print("output= ",score)