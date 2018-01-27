# DATA PREPROCESSING
#
dataset <- read.csv('Position_Salaries.csv')
dataset <- dataset[2:3]
#
# DATA PREPROCESSING END

# Fit Regression model to dataset
library(rpart)
regressor <- rpart(formula = Salary ~ .,
                   data = dataset,
                   control = rpart.control(minsplit = 1))

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
  ggtitle("Decision Tree Regression") +
  xlab("Position Level") + 
  ylab("Salary ($)")