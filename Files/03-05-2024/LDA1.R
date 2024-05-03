# Linear Discriminant Analysis (LDA)
LDA1 <- read_excel("D:/Dhruva/LDA1.xlsx")
attach(LDA1)
library(MASS)
ldaout <- lda(Buyer~Durability+Mileage+`Interior Design`+Look,data = LDA1)
summary(ldaout)
ldaout
# Predictive Model
ldapred <- predict(ldaout,LDA1)
ldapred
ldaclass <- ldapred$class
ldaclass
# Confusion Matrix
ldatable <- table(ldaclass,LDA1$Buyer)
ldatable
accur <- sum(diag(ldatable))/sum(ldatable)*100
accur

