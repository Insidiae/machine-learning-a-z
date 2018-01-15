# DATA PREPROCESSING START
#
dataset <- read.csv('Salary_Data.csv')
library(caTools)
set.seed(423)
split <- sample.split(dataset$Salary, SplitRatio = 2/3)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)
#
# DATA PREPROCESSING END

# Simple Linear Regression
# Fit Simple Linear Regression to Training Set
regressor <- lm(formula = Salary ~ YearsExperience,
               data = training_set)

# Predict Test Set Results
y_pred <- predict(regressor, newdata = test_set)

# Visualize Simple Linear Regression Model
# You need the package "ggplot2" for this.
library(ggplot2)

# Create a new ggplot
# Generate scatter plot for training data and add it to the ggplot
# visualize regression line and add it to the ggplot
# Add Titles and Axis Labels
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             color = "red") +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)), 
            color = "blue") + 
  ggtitle("Salary vs Years Experience (Training Set)") +
  xlab("Years of Experience") + 
  ylab("Salary ($)")

# Visualize Regression Model vs Test Data
ggplot() + 
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             color = "green") +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)), 
            color = "blue") + 
  ggtitle("Salary vs Years Experience (Test Set)") +
  xlab("Years of Experience") + 
  ylab("Salary ($)")