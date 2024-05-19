# Multiple Linear Regression
MR1 <- read_excel("D:/Dhruva/MR1.xlsx")
attach(MR1)
str(MR1)
# Model
Model<-lm(Buying~Attitude+Perception+Awarness+Cost+Rating,data = MR1)
plot(Model)
par(mfrow=c(2,2))
plot(Model)
library(car)
vif(Model)
cor(MR1)
summary(Model)
anova(Model)


plot(Model)
library(car)
vif(Model)
shapiro.test(Model$residuals)
