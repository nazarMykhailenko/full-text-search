from generate_keywords import generate_keywords

class Searcher:
	def __init__(self, articles):
		self.articles = articles
		self.keywords = None
		self.index_to_article = None
		self.file_name = None

	def list_to_file(self, file_name): 
		with open(file_name, 'w', encoding='utf-8') as file:
			for element in self.articles:
				file.write(str(element) + '\n')

		self.file_name = file_name

	def set_keywords(self):
		self.keywords, self.index_to_article = generate_keywords(self.file_name)

	def single_word_search(self, target):
		result = [] 
		
		for i in self.keywords[target]:
			result.append(self.index_to_article[i])
			
		return result 


	

