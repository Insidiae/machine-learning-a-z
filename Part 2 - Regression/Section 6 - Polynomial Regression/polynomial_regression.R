dataset <- read.csv('Position_Salaries.csv')
dataset <- dataset[2:3]

# Fit linear regression model to dataset
lin_reg <- lm(formula = Salary ~ Level, data = dataset)

# Add new columns corresponding to polynomial factors
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4

# Fit polynomial model to dataset
poly_reg <- lm(formula = Salary ~ ., data = dataset)

# Visualize Linear vs Polynomial Regression Models
library(ggplot2)
ggplot() + 
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset), 
                color = "red")) + 
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset), 
                color = "blue")) +
  geom_point(aes(dataset$Level, y = dataset$Salary),
             color = "red") +
  scale_colour_manual(values = c("green", "blue"), name="Model Type",
                      labels = c("Polynomial", "Linear")) +
  ggtitle("Linear vs Polynomial Regression Predictions: Salary vs Position") +
  xlab("Position Level") + 
  ylab("Salary ($)")