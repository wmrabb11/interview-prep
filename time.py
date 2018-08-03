# time = [start_time, stop_time]
# set_of_times = [ [start, stop], [start, stop], etc]

def find_time_better( set_of_times ):
	for i in xrange(0, len(set_of_times)):
		for j in xrange(i + 1, len(set_of_times)):
			time = set_of_times[i]
			time_two = set_of_times[j]
			if time == time_two:
				return False
			elif time[0] > time_two[0] and time[0] < time_two[1]:
				return False
			elif time[1] > time_two[0] and time[1] < time_two[1]:
				return False
	return True

set_of_time = [[1, 3], [4, 5]]
print find_time_better(set_of_time)
