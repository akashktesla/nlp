import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def extract_subject_object_verb(text):
    doc = nlp(text)
    
    results = []

    for sent in doc.sents:
        subj = []
        obj = []
        verb = []

        for token in sent:
            print(token,token.dep_)
            # Extract subject
            if "subj" in token.dep_:
                subj.append(token.text)
            
            # Extract object
            if "obj" in token.dep_:
                obj.append(token.text)
            
            # Extract verb
            if "VERB" in token.pos_:
                verb.append(token.text)
        
        results.append((subj, verb, obj))
    
    return results

def convert_to_lemma(text):
    doc = nlp(text)
    lemma_doc = " ".join(token.lemma_ for token in doc)
    return lemma_doc

def extract_dependecy(text):
    doc = nlp(text)
    returns = {}
    for sent in doc.sents:
        for token in sent:
            try:
                if str(token.head) != token.text:
                    returns[token.head].append(token)
            except:
                if str(token.head) != token.text:
                    returns[token.head] = [token]

    print(returns)
    for i in returns:
        print(returns[i])
        for j in returns[i]:
            print(j,j.pos_)
    return returns

# Example sentence
sentence = "I love apples and oranges"
extract_dependecy(sentence)
# sentence = convert_to_lemma(sentence)
# result = extract_subject_object_verb(sentence)
# print(result)
