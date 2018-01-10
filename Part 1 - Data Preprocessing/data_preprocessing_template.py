# Data Preprocessing

# Importing Libraries
# NOTE: press Ctrl+I to view additional info about these libraries
import numpy as np
import matplotlib.pyplot as plt
# pandas: imports the dataset
import pandas as pd
# sklearn.preprocessing.Imputer: handles missing values
from sklearn.preprocessing import Imputer
# sklearn.preprocessing.LabelEncoder: handles Categorical Data
# sklearn.preprocessing.OneHotEncoder: separates categories into their own columns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

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