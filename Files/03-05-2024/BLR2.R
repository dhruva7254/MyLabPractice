BLR2 <- read_excel("D:/Dhruva/BLR2.xlsx")
attach(BLR2)
summary(BLR2)
blrmod2 <- glm(Selection~.,data = BLR2,family = "binomial")
blrmod2
summary(blrmod2)
res1 <- predict(blrmod2,BLR2,type = "response")
res1
table(Actualvalue=BLR2$Selection,Predictedvalue=res1>0.5)
(12+22)/40 # accuracy




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
