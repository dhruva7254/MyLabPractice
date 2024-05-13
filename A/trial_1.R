EmployeeAttrition <- read.csv("C:/Users/dbda/Downloads/EmployeeAttrition.csv")
data <- iris
head(iris)
head(iris$Sepal.Length)
qaz <- array(data = NA, dim=c(3,4))
qaz
as.data.frame
M1=matrix(c(1,2,3,4),nrow = 2)
M1
M2=matrix(c(1,2,3,4),nrow = 1)
M2
df <- as.data.frame(M1)
str(df)
df
print(df$V1)
is.data.frame(df)
data = iris
iris
ncol(iris)
nrow(iris)
library(ggplot2)
ggplot(data,aes(1:150,Sepal.Length)) + geom_line()
df_1 <- read.csv("D:\A\R Programming\R Programming\data\76_attributes_heartdiseases.csv")
X76ah <- read_excel("data/76_attributes_heartdiseases.csv")
View(X76_attributes_heartdiseases)
df_2 <- read.csv("data/76_attributes_heartdiseases.csv")
df_2
summary(df_2)
ggplot()
