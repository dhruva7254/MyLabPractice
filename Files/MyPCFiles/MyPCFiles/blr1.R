# output has only 0 and 1 so we call it binary
# Binary Logistic Regression
BLR1 <- read_excel("D:/Dhruva/BLR1.xlsx")
attach(BLR1)
head(BLR1)
tail(BLR1)
summary(BLR1)
# Model Binary Logistics
blrmod <- glm(type~.,data = BLR1,family = "binomial") # binomial because only 2 categories 0 & 1 otherwise multinomial 
blrmod
summary(blrmod)
# null deviance (without any variables) error
# residual deviance (all variables) error reduces
blrmod1 <- glm(type~skin+bmi,data = BLR1,family = "binomial")
summary(blrmod1)
res <- predict(blrmod,BLR1,type = "response")
res
head(BLR1)
head(res)
# Confusion Matrix
table(Actualvalue=BLR1$type,Predictedvalue=res>0.5)
(6+14)/30 # accuracy
table(Actualvalue=BLR1$type,Predictedvalue=res>0.4)
table(Actualvalue=BLR1$type,Predictedvalue=res>0.3)
(4+18)/30
library(ROCR)
ROCRPred = prediction(res,BLR1$type)
ROCRPref <- performance(ROCRPred,"tpr","fpr")
plot(ROCRPref,colorize=TRUE,print.cutoff.at=seq(0.1,by=0.1))
library(rcompanion)
nagelkerke(blrmod)
Y = exp(y)/(1+exp(y))
