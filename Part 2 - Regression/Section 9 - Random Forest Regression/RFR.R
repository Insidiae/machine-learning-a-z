# DATA PREPROCESSING
#
dataset <- read.csv('Position_Salaries.csv')
dataset <- dataset[2:3]
#
# DATA PREPROCESSING END

# Fit Regression model to dataset
library(randomForest)
set.seed(423)
regressor_10 <- randomForest(x = dataset[1],
                          y = dataset$Salary,
                          ntree = 10)
regressor_100 <- randomForest(x = dataset[1],
                             y = dataset$Salary,
                             ntree = 100)
regressor_200 <- randomForest(x = dataset[1],
                             y = dataset$Salary,
                             ntree = 200)

# Smoothen Polynomial Model Curve
x_grid <- seq(min(dataset$Level), max(dataset$Level), 0.01)
x_grid_poly <- data.frame(Level = x_grid)

# Visualize Regression model
library(ggplot2)
ggplot() + 
  geom_line(aes(x = x_grid, y = predict(regressor_10, newdata = x_grid_poly), 
                color = "magenta4")) + 
  geom_line(aes(x = x_grid, y = predict(regressor_100, newdata = x_grid_poly), 
                color = "green")) +
  geom_line(aes(x = x_grid, y = predict(regressor_200, newdata = x_grid_poly), 
                color = "blue")) +
  geom_point(aes(dataset$Level, y = dataset$Salary),
             color = "red") +
  scale_colour_manual(values = c("magenta4", "green", "blue"), name="Model Type",
                      labels = c("200 Trees","100 Trees", "10 Trees")) +
  ggtitle("Random Forest Regression") +
  xlab("Position Level") + 
  ylab("Salary ($)")

# Predict Results
y_pred10 <- predict(regressor_10, newdata = data.frame(Level = 6.5))
y_pred100 <- predict(regressor_100, newdata = data.frame(Level = 6.5))
y_pred200 <- predict(regressor_200, newdata = data.frame(Level = 6.5))