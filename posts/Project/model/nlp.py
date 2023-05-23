import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def vectorizer(df, text_column):
    """
    Vectorize the text column
    """
    vect = TfidfVectorizer()
    vect.fit(df[text_column])
    return vect


