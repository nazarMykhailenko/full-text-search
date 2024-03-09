def get_articles(file_name):
	articles = []
	
	with open(file_name, 'r', encoding='utf-8') as file:
		articles = [line.strip() for line in file]

	return articles