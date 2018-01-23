# DATA PREPROCESSING START
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cross_validation import train_test_split
# from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder
# from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])"""

"""labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
onehotencoder_x = OneHotEncoder(categorical_features = [0])
X = onehotencoder_x.fit_transform(X).toarray()"""

"""X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""
#
# DATA PREPROCESSING END
#
# NONLINEAR REGRESSION START
#
regressor = .....
y_pred = regressor.predict(.....)

# OPTIONAL: smoothen the curve graphs by adding more X-values
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)

plt.scatter(X, y, color="red")
pred_graph, = plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title("Insert Title Here")
plt.legend(handles=[pred_graph])
plt.xlabel("Insert Label Here")
plt.ylabel("Insert Label Here")
plt.show()
# 
# NONLINEAR REGRESSION END