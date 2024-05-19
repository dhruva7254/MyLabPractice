# Simple Linear Regression
Simple_Linear_Regression_1 <- read_excel("D:/Dhruva/Simple_Linear_Regression_1.xlsx")
attach(Simple_Linear_Regression_1)
str(Simple_Linear_Regression_1)
# Normality
shapiro.test(Compensation)
shapiro.test(Performance)
# Outliers
boxplot(Compensation)
boxplot(Performance)
# Linearity
plot(Compensation,Performance)
# Simple linear regression
Model<-lm(Performance~Compensation,data = Simple_Linear_Regression_1) 
# lm -> linear model
summary(Model)
anova(Model) # to find the best fitted line
cor(Compensation,Performance)
Model$residuals
shapiro.test(Model$residuals)
abline(Model)
plot(Model)
par(mfrow=c(2,2))
plot(Model)

