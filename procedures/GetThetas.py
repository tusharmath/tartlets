from autobahn.asyncio.wamp import ApplicationSession
from autobahn.asyncio.wamp import ApplicationRunner
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd

class ThetaServer(ApplicationSession):
    def onJoin(self, details):
        def getTheta(adList):
            return x

        self.register(now, 'com.thetaserver.gettheta')

runner = ApplicationRunner(url=u"ws://localhost:8080/ws", realm=u"realm1")
runner.run(TimeServer)
# link to the training data of ad
train_ad = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
X = train_ad[['TV', 'Radio']]
y = train_ad['Sales']

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
