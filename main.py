class FlatIterator:

	def __init__(self, nested_list):
		self.nested_list = nested_list
		self.copy_nested_list = self.nested_list
		self.list_ = []
		self.index = 0
		self.ind = 0

	def __iter__(self):
		return self

	def __next__(self):
		if not self.list_:
			self.index +=1
			if len(self.copy_nested_list) < self.index:
				raise StopIteration
			self.list_ = self.copy_nested_list[(self.index)-1]
			self.list_.reverse()
		return self.list_.pop()



nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
for item in FlatIterator(nested_list):
	print(item)


# flat_list = [item for item in FlatIterator(nested_list)]
# print(flat_list)

print()
print()


def flat_generator(nested_list):
	for list in nested_list:
		for item in list:
			yield item

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]
for item in  flat_generator(nested_list):
	print(item)