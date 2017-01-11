import Base

testList = [1, 15, 18, 1, 11]


total = 0
counter = 0
for i in testList[::-1]:
	total += i * (26 ** counter)
	counter += 1
print total



testNum = str(total)
runFlag = True



answerList = []


while runFlag:
	counter = 0
	remainder = ""
	secondRow = ""

	print testNum
	for i in testNum:
		counter += 1
		secondRow += str (int(remainder + i) / 26)
		if (len(testNum) == counter):
			answerList.append(int(remainder + i) % 26)
		else:
			remainder = str (int(remainder + i) % 26)
			print secondRow


	if(int(secondRow) == 0):
		runFlag = False
	
	testNum = secondRow




print answerList[::-1]


testList = Base.convertToBase(31, 3)
print testList

newNum = Base.convertFromBase(testList, 3)
print newNum
