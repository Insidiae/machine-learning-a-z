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

# Optimize MLR Model using Backward Elimination
# Start with including all features of the dataset
# regressor_opt <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
#                 data = dataset)
# Select Significance Level for features to stay in
# e.g.: SL = 0.05

# summary(regressor_opt)
# compare P-values (Pr(>|t|)) to SL
# if highest P-value > SL, remove the feature with that P-value
# Re-fit the regressor

# Re-run this code until all features with P-values > SL are removed
# NOTE: summary(regressor_opt) makes things easier for us here.
# Asterisks (*) are added when P-values are lower than 0.05.
# (Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1)
# regressor_opt <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
#                     data = dataset)
# regressor_opt <- lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
#                     data = dataset)
regressor_opt <- lm(formula = Profit ~ R.D.Spend,
                    data = dataset)
summary(regressor_opt)