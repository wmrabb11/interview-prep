
def better_except_itself( array ):
	gcd = 1
	zero_count = 0
	for item in array:
		if item != 0:
			gcd *= item
		else:
			zero_count += 1
	for i in xrange(0, len(array)):
		if array[ i ] == 0 and zero_count <= 1:
			array[ i ] = gcd
		elif array[ i ] != 0 and zero_count == 1:
			array[ i ] = 0
		elif array[ i ] == 0:
			array[ i ] = 0
		elif zero_count > 1:
			array[ i ] = 0
		else:
			array[ i ] = gcd / array[ i ]

	return array

int_list = [1, 3, 10]

print better_except_itself(int_list)
