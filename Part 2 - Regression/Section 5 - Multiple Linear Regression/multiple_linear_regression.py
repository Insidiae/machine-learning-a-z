# DATA PREPROCESSING START
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

labelencoder_X = LabelEncoder()
X[:, -1] = labelencoder_X.fit_transform(X[:, -1])
onehotencoder_x = OneHotEncoder(categorical_features = [-1])
X = onehotencoder_x.fit_transform(X).toarray()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 423)
#
# DATA PREPROCESSING END

# Multiple Linear Regression
# Fit Multiple Linear Regression model to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict Test Set results
y_pred = regressor.predict(X_test)

# Optimize model using Backward Elimination
import statsmodels.formula.api as sm
# Append a column on 1s to X
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)

# Generate a matrix of optimal features for X
# Start with including all of X's features
# X_opt = X[:, [0, 1, 2, 3, 4, 5, 6]]
# Select a Significance Level for features to stay in
# e.g.: SL = 0.05
# If highest P-value > SL, remove the feature with that P-value
# Rerun this code segment until P values < SL
X_opt = X[:, [0, 4]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()
# Code to rerun stops here

# Fit the optimal Linear Regression model using X's significant features
# Use index 3 because X_train doesn't have that column of 1s.
X_train_opt = X_train[:, [3]]
X_test_opt = X_test[:, [3]]
regressor_opt = LinearRegression()
regressor_opt.fit(X_train_opt, y_train)

# Predict Test Set results
y_pred_opt = regressor_opt.predict(X_test_opt)