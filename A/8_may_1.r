# ggplot
# geom_line()
# # geom_line() , geom_point() , geom_histgram(), 
# geom_col(), geom_bar()
#  geom_boxplot(),  geom_violin(), geom_density()
# geom_line()
# geom_bar()
# geom_boxplot()
# geom_col()
# geom_density()
# geom_histgram()
# geom_point()
# geom_violin()
data = iris
# ggplot2
library(ggplot2)
# Line Plot
ggplot(data,aes(1:150,Sepal.Length))+geom_line()
# Scatter Plot
ggplot(data,aes(Sepal.Length,Sepal.Width))+geom_point()

