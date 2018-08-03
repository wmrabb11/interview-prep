
def binary_search(array, k, size):
	first = 0
	last = size - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last)/2
		if array[midpoint] == k:
			found = True
		else:
			if k < array[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1

	return found

def practice(array, k, size):
	return binary_search(array, k, size)
