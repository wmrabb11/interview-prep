
class Item:

	def __init__(self, color, str2):
		self.color = color
		self.str2 = str2


def sort_it(items):
	red_list = []
	white_list = []
	blue_list = []
	final_list = []

	for item in items:	
		if item.color == 'red':
			red_list.append( item )
		elif item.color == 'white':
			white_list.append( item )
		elif item.color == 'blue':
			blue_list.append( item )

	final_list.append( blue_list )
	final_list.append( red_list )
	final_list.append( white_list )
	return final_list
