# DATA PREPROCESSING START
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

sc_X = StandardScaler()
X_scaled = sc_X.fit_transform(X)
sc_y = StandardScaler()
y_scaled = sc_y.fit_transform(y)
#
# DATA PREPROCESSING END
#
# NONLINEAR REGRESSION START
#
# Fit SVR Model to dataset
from sklearn.svm import SVR
regressor = SVR(kernel = "rbf")
regressor.fit(X_scaled, y_scaled)

y_pred = sc_y.inverse_transform(
        regressor.predict(sc_X.transform(np.array([[6.5]]))))

# OPTIONAL: smoothen the curve graphs by adding more X-values
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)

plt.scatter(X, y, color="red")
pred_graph, = plt.plot(X_grid,
                       sc_y.inverse_transform(regressor.predict(sc_X.transform(X_grid))),
                       color="blue", label = "SVR Model")
plt.title("Support Vector Regression")
plt.legend(handles=[pred_graph])
plt.xlabel("Position Level")
plt.ylabel("Salary ($)")
plt.show()
# 
# NONLINEAR REGRESSION END