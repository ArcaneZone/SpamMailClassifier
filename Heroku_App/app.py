import string
import time

import streamlit as st
import pickle
import nltk
import sklearn
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    ps = PorterStemmer()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email Spam Classifier")


mail = st.text_area("enter the mail")

if st.button('Predict'):

    # 1. preprocess
    transform_mail = transform_text(mail)

    # 2. vectorize
    vector_input = tfidf.transform([transform_mail])

    # 3. predict
    result = model.predict(vector_input)[0]

    with st.spinner(text='In progress'):
        time.sleep(3)
        st.success('Done')
    # 4. display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")