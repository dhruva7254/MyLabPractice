# Two samples T-test
independent_t <- read_excel("D:/Dhruva/independent_t.xlsx")
attach(independent_t)
# Assumptions
# Continous
# Normality
shapiro.test(Mumbai)
shapiro.test(Delhi)
# Independent samples t-test
t.test(Mumbai,Delhi,mu=0)
t.test(Mumbai,Delhi,mu=0,var.equal = F)
var(Mumbai)
var(Delhi)
library(car)
leveneTest(Mumbai,Delhi,mu=0)
