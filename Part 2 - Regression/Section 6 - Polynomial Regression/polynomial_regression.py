# DATA PREPROCESSING START
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
#
# DATA PREPROCESSING END

# Polynomial Regression

# Import LinearRegression class from the sklearn library
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)

X_poly = poly_reg.fit_transform(X)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualize Linear Regression vs Polynomial Regression Results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, c="red")
# Plot the regression line (colored blue)
# ...Why do these need commas though...
lin_graph, = plt.plot(X, lin_reg.predict(X), c="blue", label="Linear Prediction")
poly_graph, = plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), c="green", label="Polynomial Prediction (4th Degree)")
plt.legend(handles=[lin_graph, poly_graph])

# Add Title and Axis Labels
plt.title("Linear vs Polynomial Regression Predictions: Salary vs Position Level")
plt.xlabel("Position Level")
plt.ylabel("Salary ($)")
plt.show()

# Predict new results using Linear and Polynomial Regression
print("Linear Prediction for Position level 6.5:", lin_reg.predict(6.5))
print("Polynomial Prediction for Position level 6.5:", lin_reg_2.predict(poly_reg.fit_transform(6.5)))