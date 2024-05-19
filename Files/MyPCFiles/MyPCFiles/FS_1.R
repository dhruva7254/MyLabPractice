# Feature Selection in R
FSR_1 <- read_excel("D:/Dhruva/FSR_1.xlsx")
attach(FSR_1)
str(FSR_1)
FSR_1$class<-as.factor(FSR_1$class)
str(FSR_1)
library(Boruta)
library(mlbench)
library(caret)
library(randomForest)
set.seed(111)
baruta<-Boruta(class~.,data=FSR_1,doTrace=2)
baruta<-Boruta(class~.,data=FSR_1,doTrace=2,maxRuns=500)
print(baruta)
plot(baruta)
plot(baruta,las=2,cex.axis=0.7)
plotImpHistory(baruta)
# Tentative Fix
bor<-TentativeRoughFix(baruta)
print(bor)
attStats(baruta)
# Model
set.seed(222)
ind<-sample(2,nrow(FSR_1),replace = T,prob = c(0.6,0.4))
train<-FSR_1[ind==1,]
test<-FSR_1[ind==2,]
# random Forest Model
set.seed(333)
rf88<-randomForest(class~.,data=train)
rf88
#Prediction and Confusion matrix for 88 variables
p<-predict(rf88,test)
p
confusionMatrix(p,test$class)    
getNonRejectedFormula(baruta)
set.seed(333)
rf58<-randomForest(class~V2+V3+V5+V11+V12+V13+V14+V15+V20+V24+V25+V26+V27+V35+V36+V37+V39+V40+V41+V42+V43+V45+V46+V47+V49+V50+V51+V52+V53+V55+V57+V58+V59+V60+V66+V68+V70+V72+V73+V75+V79+V79+V82+V83+V84+V86+V87+V88, data=train)
p1<-predict(rf50,test)
confusionMatrix(p1,test$class)

getConfirmedFormula(baruta)
rf38<-randomForest(class~V2+V3+V5+V8+V11+V14+V15+V20+V24+V25+V26+V35+V37+V40+V41+V42+V43+V47+V49+V50+V52+V53+V55+V57+V58+V59+V60+V66+V68+V70+V72+V79+V83+V84+V86+V87+V88,data=train)
p2<-predict(rf38,test)
confusionMatrix(p2,test$class)

# Karl's correlation - var1(advt) & var2(sales) are continuous
# Spearmans coefficient - var1->ordinal & var2-> ordinal

# Var1-nominal , var2-nominal 
# var1-ordinal , var2-nominal
# var1-nominal , var2-ordinal

# both variable are categorical(non-metric) then we use chi-square test










