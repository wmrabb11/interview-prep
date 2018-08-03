class Tree:
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right

	

class Iterator:

	def __init__(self, root):
		self.root = root
		self.stack = []
		node = root
		while ( node != None ):
			self.stack.append(node)
			node = node.left

	def hasNext(self):
		if len(self.stack) >= 2:
			return True
		elif self.stack[0] is not None and self.stack[0].right is not None:
			return True
		else:
			return False

	def next(self):
		tmp = self.stack[0].right
		tmp1 = self.stack[0]
		self.stack.pop()
		while ( tmp != None ):
			self.stack.append(tmp)
			tmp = tmp.left
		return tmp1.val
