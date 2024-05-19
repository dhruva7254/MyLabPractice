# Correlation Analysis
# Asumptions
# Both the variables should be continous -yes
# Normality
CRA <- read_excel("D:/Dhruva/Day-9_Correlation_Simple and Multiple Regression _Stepwise Regression/Day-9_Correlation_Simple and Multiple Regression _Stepwise Regression/Correlation Analysis/CRA.xlsx")
attach(CRA)
str(CRA)
# Assumptions
# Both the variables should be continous -yes
# Normality
shapiro.test(advt)
shapiro.test(sales)
# Linearity
plot(advt,sales)
# Outliers
boxplot(advt)
boxplot(sales)
# Correlation Analysis
cor.test(advt,sales)
# cor.test(advt,sales,method = "pearson",alternative = "spearman",conf.level = 0.95)
cor.test(advt,sales,method = "spearman",conf.level = 0.95)
