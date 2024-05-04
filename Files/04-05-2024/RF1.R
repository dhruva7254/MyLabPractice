# Random Forests using R
#it is extension of decision tree 
#it is an ensemble
data("iris")
attach(iris)
str(iris)
# Data Partition
set.seed(123) # 70 / 30 
ind<-sample(2,nrow(iris),replace=T,prob = c(0.7,0.3))
nrow(iris)
ncol(iris)
train<-iris[ind==1,]
test<-iris[ind==2,]
# Random Forest
library(randomForest)
set.seed(222)
rf<-randomForest(Species~.,data = train)
print(rf)
attributes(rf)
rf$err.rate
rf$confusion
# Prediction and Confusion Matrix on Test Data
library(caret)
p1<-predict(rf,test)
head(p1)
head(iris)
head(test$Species)
library(e1071)
confusionMatrix(p1,test$Species)
# Train data
library(caret)
p2<-predict(rf,train)
head(p2)
library(e1071)
confusionMatrix(p2,train$Species)
plot(rf)
rf<-randomForest(Species~.,data = train,ntree=200,mtry=2,importance=TRUE,proximity=TRUE)
print(rf)
hist(treesize(rf),main="no. of nodes for the trees",col = "red")
varImpPlot(rf)
varImpPlot(rf,sort=T,n.var = 3,main="top 3")
importance(rf)
# Variable used no. of times
varUsed(rf)
# Partial dependence plot
partialPlot(rf,train,Petal.Length,"setosa")
partialPlot(rf,train,Petal.Width,"setosa")
partialPlot(rf,train,Petal.Length,"versicolor")
partialPlot(rf,train,Sepal.Width,"versicolor")
getTree(rf.1.labelvar = TRUE)



