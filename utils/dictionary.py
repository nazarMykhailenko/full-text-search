from collections import defaultdict, Counter

class dictionary:

	def __init__(self, length):
		self.value = {}
		self.invertedValue = {}
		self.length = length

	def append(self, el):
		if(el in self.value):
			self.value[el] += 1
		else:
			self.value[el] = 1

	def invertArray(self):
		res = defaultdict(set)
		for _, word in enumerate(self.value):
			res[self.value[word]].add(word)

		sorted_res = dict(sorted(res.items()))

		self.invertedValue = sorted_res
		return sorted_res

class DictionaryNew:
	def __init__(self, length):
		self.counter = Counter()

	def append(self, el):
		self.counter[el] += 1

	def getTopK(self, k):
		return self.counter.most_comm
	