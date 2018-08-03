
def insert_interval( new_interval, set_of_intervals ):
	# Test the lower bound of the new interval to make sure it fits
	lower_match = False
	for interval in set_of_intervals:
		if new_interval[0] >= interval[0] and new_interval[0] <= interval[1]:
			lower_match = True
			break
		elif new_interval[0] <= interval[0]:
			interval[0] = new_interval[0]

	if not lower_match:
		set_of_intervals.append(new_interval)

	# Test the upper bound of the new interval to make sure it fits
	upper_match = False
	for interval in set_of_intervals:
		if new_interval[1] <= interval[1] and new_interval[1] >= interval[0]:
			upper_match = True
			break

	if not upper_match:
		set_of_intervals[ len(set_of_intervals) - 1][1] = new_interval[1]

	return set_of_intervals

set_of_intervals = [[1, 5], [8, 10]]
new_interval = [2, 9]

print insert_interval( new_interval, set_of_intervals )
