# Naiv Bayes using R
Naive_Bayes_1 <- read_excel("D:/Dhruva/Naive_Bayes_1.xlsx")
attach(Naive_Bayes_1)
library(naivebayes)
library(dplyr)
library(ggplot2)
library(psych)
str(Naive_Bayes_1)
Naive_Bayes_1$admit<-as.factor(Naive_Bayes_1$admit)
Naive_Bayes_1$Rank<-as.factor(Naive_Bayes_1$Rank)
str(Naive_Bayes_1)
# Exploratory Data Analysis
pairs.panels(Naive_Bayes_1[-1]) 
Naive_Bayes_1%>%ggplot(aes(x=admit,y=grade,fill=admit))+geom_boxplot()+ggtitle("Box plot")
Naive_Bayes_1%>%ggplot(aes(x=admit,y=gpa,fill=admit))+geom_boxplot()+ggtitle("Box plot")
Naive_Bayes_1%>%ggplot(aes(x=grade,fill=admit))+geom_density(alpha=0.8,color="black")+ggtitle("Density Plot")
Naive_Bayes_1%>%ggplot(aes(x=gpa,fill=admit))+geom_density(alpha=0.8,color="black")+ggtitle("Density Plot")
# Data Partition
ind<-sample(2,nrow(Naive_Bayes_1),replace = T,prob = c(0.8,0.2))
train<-Naive_Bayes_1[ind==1,]
test<-Naive_Bayes_1[ind==2,]
# Model
model=naive_bayes(admit~.,data=train)
plot(model)
p=predict(model,train,type="prob")
head(cbind(p,train))
# confusion matrix
p1=predict(model,test)
tab1=table(p1,test$admit)
tab1
26/45
p2=predict(model,train)
tab2=table(p2,train$admit)
tab2
sum(diag(tab2))/sum(tab2)
1-sum(diag(tab2))/sum(tab2)
# Exploratory Data Analysis
train%>%filter(admit=="0")%>%summarise(mean(grade),sd(grade))
train%>%filter(admit=="0")%>%summarise(mean(gpa),sd(gpa))
train%>%filter(admit=="1")%>%summarise(mean(grade),sd(grade))
train%>%filter(admit=="1")%>%summarise(mean(gpa),sd(gpa))



