import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd

# link to the training data of ad
df_ad = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
X = df_ad[['TV', 'Radio']]
y = df_ad['Sales']

# Create linear regression object
lRegression = linear_model.LinearRegression()

# Train the model using the training sets
lRegression.fit(X, y)

# The coefficients
print('Coefficients: \n', lRegression.coef_)

print('Value of x is')
print(X)
# Prediction for a certain value of X
x = [100, 50]
print("Prediction for x is ")
print(lRegression.predict(x))
