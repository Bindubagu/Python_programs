num = int(input("Enter the number:"))
i = 0
while i <= num:
	temp = i
	x = temp % 10
	temp = temp // 10
	if temp == 0:
		print(i,end = " ")
	else:
		while temp != 0:
			y = temp % 10
			temp = temp // 10
			if x == y-1 or x == y+1:
				x = y
				if temp == 0:
					print(i,end = " ")
			else:
				break
	i += 1
