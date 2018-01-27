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
# RANDOM FOREST REGRESSION START
#
from sklearn.ensemble import RandomForestRegressor
regressor_10 = RandomForestRegressor(n_estimators = 10,
                                  random_state = 423)
regressor_100 = RandomForestRegressor(n_estimators = 100,
                                  random_state = 423)
regressor_200 = RandomForestRegressor(n_estimators = 200,
                                  random_state = 423)
regressor_10.fit(X, y)
regressor_100.fit(X, y)
regressor_200.fit(X, y)

y_pred_10 = regressor_10.predict(6.5)
y_pred_100 = regressor_100.predict(6.5)
y_pred_200 = regressor_200.predict(6.5)

# OPTIONAL: smoothen the curve graphs by adding more X-values
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape(len(X_grid), 1)

plt.scatter(X, y, color="red")
pred_graph_10, = plt.plot(X_grid, regressor_10.predict(X_grid), color="blue",
                       label = "RFR Model (10 Trees)")
pred_graph_100, = plt.plot(X_grid, regressor_100.predict(X_grid), color="green",
                       label = "RFR Model (100 Trees)")
pred_graph_200, = plt.plot(X_grid, regressor_200.predict(X_grid), color="magenta",
                       label = "RFR Model (200 Trees)")
plt.title("Random Forest Regression")
plt.legend(handles=[pred_graph_10, pred_graph_100, pred_graph_200])
plt.xlabel("Position Level")
plt.ylabel("Salary ($)")
plt.show()
# 
# RANDOM FOREST REGRESSION END