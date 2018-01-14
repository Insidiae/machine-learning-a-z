
# DATA PREPROCESSING START
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cross_validation import train_test_split
# from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
#
# DATA PREPROCESSING END

# Simple Linear Regression

# Import LinearRegression class from the sklearn library
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

# Fit regressor model to training data
regressor.fit(X_train, y_train)

# Predict target values from the test set
y_pred = regressor.predict(X_test)

# Visualize training set results
# Generate scatter plot for training data (colored red)
plt.scatter(X_train, y_train, c="red")
# Plot the regression line (colored blue)
plt.plot(X_train, regressor.predict(X_train), c="blue")
# Add Title and Axis Labels
plt.title("Salary vs Years Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary ($)")
plt.show()

# Visualize test set results
# Generate scatter plot for test data (colored green)
plt.scatter(X_test, y_test, c="green")
# Plot the regression line (colored blue)
plt.plot(X_train, regressor.predict(X_train), c="blue")
# Add Title and Axis Labels
plt.title("Salary vs Years Experience (Test Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary ($)")
plt.show()