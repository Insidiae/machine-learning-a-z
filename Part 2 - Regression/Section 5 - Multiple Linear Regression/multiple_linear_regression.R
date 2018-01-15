# DATA PREPROCESSING START
#
dataset <- read.csv('50_Startups.csv')

dataset$State <- factor(dataset$State,
                         levels = c('New York', 'California', 'Florida'),
                         labels = c(1, 2, 3))

library(caTools)
set.seed(423)
split <- sample.split(dataset$Profit, SplitRatio = 0.8)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)
#
# DATA PREPROCESSING END

# Multiple Linear Regression
# Fit Multiple Linear Regression model to Training Set
regressor <- lm(formula = Profit ~ .,
               data = training_set)

# Predict Test Set Results
y_pred <- predict(regressor, newdata = test_set)
