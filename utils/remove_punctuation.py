import string

def remove_punctuation(input_string):
    translation_table = str.maketrans("", "", string.punctuation)
    cleaned_string = input_string.translate(translation_table)
    return cleaned_string