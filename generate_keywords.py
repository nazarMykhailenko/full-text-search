from tqdm.auto import tqdm
from collections import defaultdict

from utils.tokenizer import Tokenizer
from utils.get_articles import get_articles


def generate_keywords(file_name): 
  keywords_map = defaultdict(set)
  index_to_article = [None] * len(articles)

  articles = get_articles(file_name)
    

  for i, elem in enumerate(tqdm(articles)):
    elem_tokens = Tokenizer.tokenize(elem)
    
    for word in elem_tokens:
      keywords_map[word].add(i)
      index_to_article[i] = elem

  return keywords_map, index_to_article



  

# if word in keywords_map:
#   prev_elem = keywords_map[word]
#   if isinstance(prev_elem, list):
#     prev_elem.append(elem)
#   else:
#     keywords_map[word] = [prev_elem, elem]
# else:
#           keywords_map[word] = elem
  
