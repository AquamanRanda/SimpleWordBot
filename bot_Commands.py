from PyDictionary import PyDictionary
import nltk
from nltk.corpus import wordnet as wn
import botfile as ff
dict = PyDictionary()

def hello():
    print("Hello I am Mr.Word")
def bye():
    print("Thank you for using Mr.word. Bye folks!")
def meaning(str):
    mean = dict.meaning(str)
    j = 0
    return (mean)

def synonyms(str):
    synonyms = []
    antonyms = []

    for syn in wn.synsets(str):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    return set(synonyms)


def antonyms(str):
    synonyms = []
    antonyms = []

    for syn in wn.synsets(str):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    return set(antonyms)



meaning('hello')