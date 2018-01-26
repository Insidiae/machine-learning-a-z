dataset <- read.csv('Position_Salaries.csv')
dataset <- dataset[2:3]

# Fit Regression model to dataset
library(e1071)
regressor <- svm(formula = Salary ~ .,
                 data = dataset,
                 type = "eps-regression")

y_pred <- predict(regressor, data.frame(Level = 6.5))

# Smoothen Polynomial Model Curve
x_grid <- seq(min(dataset$Level), max(dataset$Level), 0.1)
x_grid_poly <- data.frame(Level = x_grid)

# Visualize Regression model
library(ggplot2)
ggplot() + 
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = x_grid_poly)),
            color = "blue") +
  geom_point(aes(dataset$Level, y = dataset$Salary),
             color = "red") +
  ggtitle("Support Vector Regression") +
  xlab("Position Level") + 
  ylab("Salary ($)")
