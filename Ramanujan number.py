listxy = []
sum = 0
for x in range(1,26):
    listsum = []
    for y in range(1,26):
        if y <= x:
            sum = 0
            listsum.append(sum)
        else:
            sum = x**3 + y**3
            listsum.append(sum)
            #print("sum = ",sum,end = " ")
#            print("x = ",x,end = " ")
#            print("y = ",y)
    listxy.append(listsum)

#for i in range(25): 
#    for j in range(25): 
#        print(listxy[i][j], end = " ") 
#    print()
    
min = listxy[1][1]
z = 1
for i in range(25):
	for j in range(25):
		if listxy[i][j] > 0:
			for x in range(25):
				for y in range(25):
					if listxy[x][y] > 0:
						if x == i and y == j:
							continue
						else:
							if listxy[x][y] == listxy[i][j]:
								if listxy[x][y] > min:
									min = listxy[x][y]
									print(z,". ",min," = ",x + 1,"^3 + ",y + 1,"^3 = ",i + 1,"^3 + ",j + 1,"^3")
									z = z +1