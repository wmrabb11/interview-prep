
def move_zeroes( list_of_ints ):
	zeroes = []
	my_list = list_of_ints
	for num in list_of_ints:
		if num == 0:
			zeroes.append(num)
			my_list.remove(num)
	my_list.append(zeroes)
	return my_lis


def my_zeros( lst ) :
	i = 0
	for x in lst :
		if x != 0 :
			lst[i] = x
			i += 1
	for j in range(i, len(lst)) :
		lst[j] = 0
	return lst

print my_zeros( [1, 0, 3, 0, 1] )
