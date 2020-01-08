from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "she is beautiful. think different before you speak"

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example)
filteredwords = []
for w in word_tokens:
    if w not in stop_words:
        filteredwords.append(w)

print(filteredwords)
