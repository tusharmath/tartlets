import numpy as np
from sklearn import datasets, linear_model
import pandas as pd

def fit_model(X,y):
    lRegression = linear_model.LogisticRegression()
    lRegression.fit(X, y)
    return lRegression

def get_ctr(lRegression,X):
    return lRegression.predict_proba(X)[0][1]

