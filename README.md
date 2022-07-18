# Introduction

## What is Spam Mail Classifier ?
Spam Mail Classifier uses Machine learning model(NLP) to detect Spam Mails. We tried out multiple classifier algorithms such as SVM, Naive Bayes, XGBoost, Random Forest, etc, to classify our mails into Spam or Ham mail.

## Need of Spam Mail Classifier ?
Now a days, spam is progressively being viewed as a more severe messaging threat, as it is coming to be used to deliver worms, viruses, and Trojans as well as rooks of more directly financial nature. Spammers often trick even the sharpest of e-mail users into opening these messages.


### Requirements
* Python
* Jupyter
* NLTK
* SkLearn
* Matplotlib
* Seaborn

### Procedure
1. Importing Basic Modules - Pandas, NumPy
2. Loading the Dataset
3. Data Pre-Processing
    1. Data Cleaning
    2. Data Transformation
4. Exploratory Data Analysis
5. Added Columns such as wordCount, CharacterCount, SentenceCount for improved dataset. 
6. Text Preprocessing
    1. Lower case
    2. Tokenization
    3. Removing special characters
    4. Removing stop words and punctuation
    5. Stemming
7. Model Building
    1. Vectorization
    2. Splitting into training and testing dataset.
    3. Tried and tested multiple classifier models on the basis of precision and accuracy.
    4. We Choose the best model on the basis of precision and accuracy and we found that Multinomial Naive Bayes gave us the highest precision & accuracy.
8. Building Frontend
    1. Used Streamlit for building frontend of our website.
    2. Integrated our model with Frontend using Pickle.
    3. Performed 4 steps with our input data
        1. Preprocessing
        2. Vectorization
        3. Prediction
        4. Displaying Result 
9. Deployment on Heroku


## Screenshots

![Screenshot1](https://github.com/ArcaneZone/SpamMailClassifier/blob/main/Assets/spampng.png?raw=true)

![Screenshot2](https://github.com/ArcaneZone/SpamMailClassifier/blob/main/Assets/notspam.png?raw=true)
