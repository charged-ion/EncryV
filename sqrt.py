def sqrt(val):
	x = 0.0
	if val < 1:
		x = 2.0
	elif val > 0:
		while x ** 2 <= val:
			if x ** 2 == val:
				return x
			x += 1
		x -= 1
	
	x2 = 0.0

	while True:
		x = val / x
		x = ((val / x) + x) / 2
		if x ** 2 == val:
			return x
		elif x2 == x:
			print "wtf"
			return x
		x2 = x


print sqrt(5)
