import xml.etree.ElementTree as ET
import mwparserfromhell
from tqdm.auto import tqdm

def parse_articles(max, path):
  '''
  generate_index does blah blah blah.

    :param max: describe about parameter p1
    :param p2: describe about parameter p2
    :param p3: describe about parameter p3
    :return: describe what it returns
  ''' 
  
  context = ET.iterparse(path, events=("start", "end"))

  context = iter(context)
  event = next(context)

  articles = []
  i = 0
  for event, elem in tqdm(context):  
    if elem.tag.endswith('text') and event=='end':  
      parsed_wiki_text = mwparserfromhell.parse(elem.text)
      final_text = parsed_wiki_text.strip_code().replace('\n',' ')
      articles.append(final_text)
      i += 1  

    if i == max:
      break

  return articles