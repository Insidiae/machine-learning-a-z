# Data Preprocessing

# Import the dataset
dataset = read.csv('Data.csv')

# Handle Missing Data
# If data is missing(na), replace it with the mean of the existing values in that column.
# Else, just return the same value :)
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

# Encode Categorical Data
# NOTE: to view additional info about a function, just press F1
# NOTE: even if you use 'numeric' labels, the values are still considered as non-numeric.
dataset$Country = factor(dataset$Country, 
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased, 
                         levels = c('No', 'Yes'),
                         labels = c(0, 1))

# Split dataset into training and test sets
# For this, we need to import library caTools
# to install caTools, run "install.packages('caTools')"
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# sample.split returns bool values for each row in the data set
# now you can split the dataset according to the values returned by sample.split
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# Since columns 1 and 4 of the dataset are non-numeric, we'll exclude them from the scaling.
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])