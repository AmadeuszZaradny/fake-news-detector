from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
stop_words = list(set(stopwords.words('english')))
porter_stemmer = PorterStemmer()


def stemming_tokenizer(str_input):
    alphabetic_words = extract_only_alphabetic_words(str_input.lower())
    relevant_words = list(filter(lambda word: word not in stop_words, alphabetic_words))
    return [porter_stemmer.stem(word) for word in relevant_words]


def extract_only_alphabetic_words(words):
    return re.findall(r'\b[a-zA-Z]+\b', words)
