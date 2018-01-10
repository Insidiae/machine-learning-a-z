# Data Preprocessing

# Importing Libraries
# NOTE: press Ctrl+I to view additional info about these libraries
import numpy as np
import matplotlib.pyplot as plt
# pandas: imports the dataset
import pandas as pd
# sklearn.preprocessing.Imputer: handles missing values
# sklearn.preprocessing.LabelEncoder: handles Categorical Data
# sklearn.preprocessing.OneHotEncoder: separates categories into their own columns
# sklearn.preprocessing.StandardScaler: handles Feature Scaling
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
# sklearn.cross_validation.train_test_split: splits data into training and test sets
from sklearn.cross_validation import train_test_split



# Importing the dataset
dataset = pd.read_csv('Data.csv')
# dataset.iloc[rows, cols].values
# selects certain columns from dataset
# to select all rows/columns, use ':'
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# Handle missing data (NaN)
# common practice: use the mean of other existing data for that variable.
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
# fit the imputer to the matrix with missing data
imputer = imputer.fit(X[:, 1:3])
# apply the imputer to that matrix
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Categorical Data: Encode string data to numbers
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)
# Separate categories into their own columns
onehotencoder_x = OneHotEncoder(categorical_features = [0])
X = onehotencoder_x.fit_transform(X).toarray()

# Split dataset to into Training and Test Sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
# To get the same values as the lecture's, we need to use the same random seed (random_state).

# Feature Scaling
# scales the ranges of values in your dataset
# standardization ((x - x_mean) / x_standard_deviation) 
# vs normalization ((x - x_min)/ (x_max - x_min))
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
# fit_transform actually calls two functions fit() and transform
# Since fit() is already called for X (in the training set),
# we just need to call transform() for the other set.
X_test = sc_X.transform(X_test)