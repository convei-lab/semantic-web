import nltk 
from nltk.corpus import wordnet

def get_synonyms_and_antonyms(word):
    synonyms = [] 
    antonyms = [] 

    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
            if l.antonyms(): 
                antonyms.append(l.antonyms()[0].name()) 
    

    synonyms = list(set(synonyms))
    antonyms = list(set(antonyms))

    return synonyms, antonyms

if __name__=='__main__':
    word = 'good'
    synonyms, antonyms = get_synonyms_and_antonyms(word)
    print(synonyms)
    print(antonyms)