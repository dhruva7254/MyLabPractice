# MLR2 multiple Linear Regression
MLR2 <- read_excel("D:/Dhruva/MR1.xlsx")
attach(MLR2)
str(MLR2)
# Model
mlrmodel <- lm(Buying~.,data = MLR2)
plot(mlrmodel)
# multicollinearity
library(car)
mlrvif <- vif(mlrmodel)
T = 1/mlrvif
# Assumptions are Satisfied
anova(mlrmodel)
summary(mlrmodel)
mlr1model <- lm(Buying~Awarness+Attitude+Perception,data = MLR2)
summary(mlr1model)
# regression equation
# y(PD) = 0.466(Awa)+0.379(Att)+0.197(Per)+0.508
