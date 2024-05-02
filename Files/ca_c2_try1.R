CSMCA <- read_excel("D:/Dhruva/Case_2_Shopping_Mall_Cluster_Analysis.xlsx")
attach(CSMCA)
dis <- dist(CSMCA)
dis
print(dis,digits = 3)
hc.c<-hclust(dis)
hc.c
plot(hc.c)
plot(hc.c,hang = -1)
member.c<-cutree(hc.c,2)
member.c
library(cluster)
kc<-kmeans(CSMCA,3)
kc
kc$cluster
aggregate(CSMCA,list(member.c),mean)
