from nltk.corpus import wordnet
syns = wordnet.synsets("culture")

##print(syns)
##
##print(syns[2])
##print(syns[2].lemmas()[0].name())
##
##print(syns[2].definition())
##print(syns[0].examples())
##print(syns[0].definition())
##
##
##synonyms = []
##antonyms = []
##
##for syn in wordnet.synsets("take"):
##    for l in syn.lemmas():
##        synonyms.append(l.name())
##        if l.antonyms():
##            antonyms.append(l.antonyms()[0].name())
##
##
##print(set(synonyms))
##print(set(antonyms))


w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('float.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('floating.n.01')
print(w1.wup_similarity(w2))


