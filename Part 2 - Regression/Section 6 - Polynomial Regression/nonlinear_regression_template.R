# DATA PREPROCESSING
#
dataset <- read.csv('Position_Salaries.csv')

# dataset$Age <- ifelse(is.na(dataset$Age),
#                      ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
#                      dataset$Age)
# dataset$Salary <- ifelse(is.na(dataset$Salary),
#                         ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
#                         dataset$Salary)
# 
# 
# dataset$Country <- factor(dataset$Country, 
#                          levels = c('France', 'Spain', 'Germany'),
#                          labels = c(1, 2, 3))
# dataset$Purchased <- factor(dataset$Purchased, 
#                          levels = c('No', 'Yes'),
#                          labels = c(0, 1))

# library(caTools)
# set.seed(123)
# split <- sample.split(dataset$Purchased, SplitRatio = 0.8)
# training_set <- subset(dataset, split == TRUE)
# test_set <- subset(dataset, split == FALSE)

# training_set[, 2:3] <- scale(training_set[, 2:3])
# test_set[, 2:3] <- scale(test_set[, 2:3])
#
# DATA PREPROCESSING END

# Fit Regression model to dataset
regressor <- .....

# Smoothen Regression Model Curve
# Smoothen Polynomial Model Curve
x_grid <- seq(min(dataset$Level), max(dataset$Level), 0.1)
x_grid_poly <- data.frame(Level = x_grid,
                          Level2 = x_grid ^ 2,
                          Level3 = x_grid ^ 3,
                          Level4 = x_grid ^ 4)

# Visualize Regression model
library(ggplot2)
ggplot() + 
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = x_grid_poly), 
                color = "blue")) +
  geom_point(aes(dataset$Level, y = dataset$Salary),
             color = "red") +
  ggtitle("Insert Title Here") +
  xlab("X Axis Label") + 
  ylab("Y Axis Label")