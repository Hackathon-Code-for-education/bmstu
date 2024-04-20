import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.compose import ColumnTransformer
from scipy.sparse import hstack
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
stop = stopwords.words()

class_names = [1, 0]

df = pd.read_csv('labeled.csv').fillna(' ')
# test = pd.read_csv('../input/test.csv').fillna(' ')

# train_text = train['comment_text']
# test_text = test['comment_text']
# all_text = pd.concat([train_text, test_text])

train, test = train_test_split(df, test_size=0.2, random_state=42)

pipeline = Pipeline(steps=[
    "features",
    ColumnTransformer([
        ("comment", CountVectorizer(stop_words=stop),"comment")
    ]),
    ('clf', LogisticRegression(random_state=SEED, solver='lbfgs', class_weight='balanced'))
])

X_train = train['comment']
y_train = train['toxic']

pipeline.fit(X_train, y_train)