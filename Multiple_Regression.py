# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:40:02 2019

@author: NeetKing
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('50_Startups.csv')

X = dataset.iloc[:, :-1].values

y = dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()

X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

X = X[:, 1:]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

print("y_pred = ",y_pred)
print("y_test = ",y_test)

print("Train : ", regressor.score(X_train, y_train)*100," %")
print("Test : ", regressor.score(X_test, y_test)*100," %")

print("Coef :",regressor.coef_)
print(regressor.intercept_)


import statsmodels.regression.linear_model as sm
X= np.append(arr = np.ones((50,1)).astype(int), values = X, axis=1) 
X_opt= X[:, [0,1,2,3,4,5]]
regressor_OLS=sm.OLS(endog = y, exog = X_opt).fit()

print(regressor_OLS.summary())


X_opt = X [:, [0,1,3,4,5]] 
regressor_OLS = sm.OLS (endog = y, exog = X_opt) .fit () 
regressor_OLS.summary ()

print(regressor_OLS.summary())

X_opt = X [:, [0,3,4,5]] 
regressor_OLS = sm.OLS (endog = y, exog = X_opt) .fit () 
regressor_OLS.summary ()

print(regressor_OLS.summary())

X_opt = X [:, [0,3,5]] 
regressor_OLS = sm.OLS (endog = y, exog = X_opt) .fit () 
regressor_OLS.summary ()

print(regressor_OLS.summary())

X_opt = X [:, [0,3]] 
regressor_OLS = sm.OLS (endog = y, exog = X_opt) .fit () 
regressor_OLS.summary ()

print(regressor_OLS.summary())
