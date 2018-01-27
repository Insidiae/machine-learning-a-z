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
#
# DECISION TREE REGRESSION START
#
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 423)
regressor.fit(X, y)
y_pred = regressor.predict(6.5)

# OPTIONAL: smoothen the curve graphs by adding more X-values
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape(len(X_grid), 1)

plt.scatter(X, y, color="red")
pred_graph, = plt.plot(X_grid, regressor.predict(X_grid), color="blue",
                       label = "DTR Model")
plt.title("Decision Tree Regression")
plt.legend(handles=[pred_graph])
plt.xlabel("Position Level")
plt.ylabel("Salary ($)")
plt.show()
# 
# DECISION TREE REGRESSION END