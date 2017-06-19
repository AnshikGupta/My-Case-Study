import nltk
import random
from nltk.tokenize import word_tokenize
#from nltk.corpus import movie_reviews
import pickle
#from nltk.classify.scikitlearn import SklearnClassifier
#from sklearn.naive_bayes import MultinomialNB,BernoulliNB

short_pos = open("positive_sentiments.txt","r").read()
short_neg = open("negative_sentiments.txt","r").read()

#short_pos = open("sample.txt","r").read()
#short_neg = open("sample.txt","r").read()

documents = []
all_words =  []
allowed_word_types = ["J"]

for r in short_pos.split('\n'):
    documents.append( (r, "pos") )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

for r in short_neg.split('\n'):
    documents.append( (r, "neg") )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())
            
save_documents = open("NBdocuments.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]

save_word_features = open("NBword_features5k.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()

def find_features(document):
    words = word_tokenize(document)
    feature = {}
    for w in word_features:
        feature[w] = (w in words)
    return feature

featuresets = [(find_features(rev),category) for (rev, category) in documents]

#print(featuresets)
random.shuffle(featuresets)

training_set = featuresets[:10000]
testing_set = featuresets[10000:]

classifier = nltk.NaiveBayesClassifier.train(training_set)

#classifier_f = open("naivebayes.pickle","rb")
#classifier = pickle.load(classifier_f)
#classifier_f.close()

print("Classifier accuracy percent:", (nltk.classify.accuracy(classifier, testing_set)))
classifier.show_most_informative_features(15)

save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
