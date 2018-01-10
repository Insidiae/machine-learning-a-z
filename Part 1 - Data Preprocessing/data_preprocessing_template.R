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
dataset$Country = factor(dataset$Country, 
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased, 
                         levels = c('No', 'Yes'),
                         labels = c(0, 1))