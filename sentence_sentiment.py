import nltk
import random
from nltk.tokenize import word_tokenize
import pickle

documents_f = open("NBdocuments.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()


word_features5k_f = open("NBword_features5k.pickle", "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()

def find_features(document):
    words = word_tokenize(document)
    feature = {}
    for w in word_features:
        feature[w] = (w in words)
    return feature

open_file = open("naivebayes.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()

def sent_analysis(text):
    feats = find_features(text)
    return classifier.classify(feats)
