# One Sample T-test
Indian_oil_ethanol <- read_excel("D:/Dhruva/Indian_oil_ethanol.xlsx")
attach(Indian_oil_ethanol)
# Assumptions
# Normality Tests: Shapiro, Lillie, Anderson
shapiro.test(`Mileage with ethanol`)
library(nortest)
lillie.test(`Mileage with ethanol`)
ad.test(`Mileage with ethanol`)
# My data satisfies the condition of normal distribution
# one Sample T-test
t.test(`Mileage with ethanol`,mu=12)
