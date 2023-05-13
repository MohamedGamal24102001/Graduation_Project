from django.shortcuts import render
import pickle 
import re
import string
import os
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk


try:
    stopwords.words
except:
    nltk.download('stopwords')

static_files_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static\\classifiers\\')

def read_pickle_file(filename):
    with open(static_files_path+filename, 'rb') as file:
        myfile = pickle.load(file)
    return myfile

def lemmatize_all_types(word):
    wnl = WordNetLemmatizer()
    word = wnl.lemmatize(word, 'a')
    word = wnl.lemmatize(word, 'v')
    word = wnl.lemmatize(word, 'n')
    return word

# Function to clean text
def clean(text):
    engstopwords = stopwords.words('english')
    # Remove URLs from text
    text = re.sub(r"https?://\w+\.\w+\.\w+", "", text).lower()
    # Remove punctuations any symbols
    text = re.sub('[^a-zA-Z ]',"",  text)
    # Check that each word is not stopword, and lemmatize it
    text = list(map(lemmatize_all_types, text.split()))
    text = [word for word in text if (word not in engstopwords)]
    text = " ".join(text)
    return text



def classify(text, model_name='model.pickle', config_file_name='config.pickle'):
    config = read_pickle_file(config_file_name)
    model = read_pickle_file(model_name)

    # Vectorizer is either tfidf or cv (CountVectorizer)
    vectorizer = config['tfidf'] 

    text = clean(text)
    text = vectorizer.transform([text])
    output = model.predict(text)[0]
    label = config['labels'][output]
    
    return label