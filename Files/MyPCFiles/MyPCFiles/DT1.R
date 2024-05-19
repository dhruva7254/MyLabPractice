# Decision Tree in R
# Data
data("iris")
attach(iris)
View(iris)
str(iris)
# Data Partition
set.seed(555)
ind<-sample(2,nrow(iris),replace = TRUE,prob = c(0.8,0.2))
train<-iris[ind==1,] # for 0.8
test<-iris[ind==2,] # for 0.2
library(party)
tree<-ctree(Species~.,train)
print(tree)
# Visualization
plot(tree)
plot(tree,type="simple")
head(train)
# Confusion Matrix for test data
p1<-predict(tree,test) # probability of test data
p1
tab1<-table(Predicted=p1,Actual=test$Species)
tab1
sum(diag(tab1))/sum(tab1) # accuracy
1-sum(diag(tab1))/sum(tab1) # error
sum(diag(tab1))/sum(tab1)*100
# Confusion Matrix for Training data
p2<-predict(tree,train) # probability of test data
p2
tab2<-table(Predicted=p2,Actual=train$Species)
tab2
sum(diag(tab2))/sum(tab2) # accuracy
1-sum(diag(tab2))/sum(tab2)
# Regression Tree
tree1<-ctree(Sepal.Length~.,train)
tree1
plot(tree1)





