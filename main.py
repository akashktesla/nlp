import spacy
import numpy as np
from spacy import displacy

# nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("en_core_web_md")
# with open("data/wiki_us.txt","r") as f:
#     text = f.read()

# doc = nlp(text)
# sentences  = list(doc.sents)
# sen1 = sentences[0]
# print(sen1)

doc = nlp("I love my child")
print(f"{doc}")
# for token in doc:
#     print(f"{token}, {token.dep_}")

#finding similarity
def find_similarity():
    word = "country"
    ms = nlp.vocab.vectors.most_similar(
        np.asarray([nlp.vocab.vectors[nlp.vocab.strings[word]]]),n=10
    )
    words = [nlp.vocab.strings[w] for w in ms[0][0]]
    distances = ms[2]
    print(words)
    doc1 = nlp("I like saltly fries and hamburgers.")
    doc2 = nlp("Fast food tastes very good.")
    print(doc1,"<->",doc2,doc1.similarity(doc2))



