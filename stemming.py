from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

example = "she is beautiful. think thinking thinked  different before you speak"
ps = PorterStemmer()

example_text = word_tokenize(example)
for w in example_text:
    print(ps.stem(w))
