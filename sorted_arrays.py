
def combine(arr1, arr2):
	i = 0
	j = 0
	k = 0
	n1 = len(arr1)
	n2 = len(arr2)
	arr3 = [0]*(n1+n2)
	while ( i < n1 and j < n2 ):
		if arr1[i] > arr2[j]:
			arr3[k] = arr1[i]
			k += 1
			i += 1
		else:
			arr3[k] = arr2[j]
			k += 1
			j += 1
	while i < n1:
		arr3[k] = arr1[i]
		k += 1
		i += 1
	while j < n2:
		arr3[k] = arr2[j]
		k += 1
		j += 1
	return arr3

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print combine(arr1, arr2)
