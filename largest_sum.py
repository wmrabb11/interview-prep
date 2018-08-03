def largest_sum(array, k):
	result = 0
	num_added = 0
	for i in range(9, 0, -1):
		for j in array:
			if i == j:
				if  num_added < k:
					result += j
					num_added += 1
				else:
					return result

print largest_sum([1, 9, 2, 8, 4], 2)
