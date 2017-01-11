def convertFromBase(values, base):
	total = 0
	counter = 0

	for i in values[::-1]:
		total += i * (base ** counter)
		counter += 1
	return total




def convertToBase(value, base):
	num = str(value)
	runFlag = True
	ansList = []

	while runFlag:
		counter = 0
		remainder = ""
		secondRow = ""

		for i in num:
			counter += 1
			secondRow += str(int(remainder + i) / base)

			if(len(num) == counter):
				ansList.append(int(remainder + i) % base)
			else:
				remainder = str(int(remainder + i) % base)

		if(int(secondRow) == 0):
			runFlag = False
		else:
			num = secondRow
	return ansList[::-1]
