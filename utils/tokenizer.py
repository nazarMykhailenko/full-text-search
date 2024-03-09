from nltk.tokenize import word_tokenize
from utils.remove_punctuation import remove_punctuation

class Tokenizer:    
    @staticmethod
    def tokenize(word: str) -> list[str]:
        return word_tokenize(remove_punctuation(word))