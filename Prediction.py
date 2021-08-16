import nltk
import pickle
from nltk.corpus import stopwords
import string


def get_pred(text):
    words = text.split(" ")
    stops = stopwords.words('english')
    punc = list(string.punctuation)
    stops = stops + punc

    useful_words = [w for w in words if not w in stops]

    vectorizer = pickle.load(open("./static/vectorizer.pickle", "rb"))
    vector = vectorizer.transform(useful_words)

    pkl_filename = "./static/pickle_model.pkl"
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    result = pickle_model.predict(vector)
    print(result)
    pos = 0
    neg = 0
    for i in range(len(result)):
        if(result[i]=='pos'):
            pos+=1
        else:
            neg+=1
    if(pos>=neg):
        return "Positive"
    else:
        return "Negative"