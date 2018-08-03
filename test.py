def helper(A, B):
	# Make a new string to hold the result
	new_str = ''
	# Keep a carry flag and set it to 0
	carry = 0
	# Loop through the characters in both A & B since they are the same length now
	for digit in xrange(len(A)):
		# Convert each CHAR to an int, only said don't convert strings to ints
		num1 = int(A[digit])
		num2 = int(B[digit])
		# Add them up including the carry flag
		result = num1 + num2 + carry
		# If the result is 2 or 3, set the carry flag so it can add it to the next column
		if result >= 2:
			carry = 1
			# Add the result to the new string (modulo because we want to add the remainder, not 2 or 3)
			new_str += '{}'.format(result % 2)
		else:
			carry = 0
			new_str += '{}'.format(result)
	# Add the carry flag to the front in case of any overflows
	new_str += str(carry)
	# Reverse back the string so it's in proper order now and return it
	return new_str[::-1]
	

def add(A, B):
	# Reverse the strings so we can add from right to left
	A = A[::-1]
	B = B[::-1]
	# Check to see which is longer and pad with zeros on the right since they are reversed
	if len(A) >= len(B):
		B += (len(A) - len(B))*'0'
		return helper(A, B)
	else:
		A += (len(B) - len(A))*'0'
		return helper(A, B)

print ' 1101'
print '+0011'
print add('1101', '11')
print '-----'
print ' 0101'
print '+1010'
print add('0101', '1010')
