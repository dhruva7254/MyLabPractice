# 02-05-2024
# Exploratory Factor Analysis
EFA1 <- read_excel("D:/Dhruva/EFA1.xlsx")
attach(EFA1)
str(EFA1) # to check whether data is continuous or not
# KMO should be > 0.5
library(psych)
r=cor(EFA1) #  all correlation coefficients between different variables
r
KMO(EFA1) # adequacy of samples ...
KMO(r)
# the sample size is adequate to run the EFA
# Bartlett test
cortest.bartlett(EFA1) # variable should be related to each other
cortest.bartlett(r) # < 0.05
# REdaS
library(REdaS)
KMOS(EFA1)
bart_spher(EFA1) # < 0.05 means H1 (alternate hypothesis) is accepted
# EFA
# principle component method
pca(r,nfactors = 10,rotate = F) # to find eigen values to find what factors to consider
mz <- pca(r,nfactors = 10,rotate = F) # there may be cross loading so rotation ... but here no rotation
# SS loadings == eigen values , eigen value should be > 1 
# Varimax method , no. of factors = 3
z=pca(r,nfactors = 3,method = regression,rotate = "varimax",scores = T) # to minimize (reduce) cross loading we use varimax
z
# total variance explained = 69%
# h2 = commonalities  ( comm > 0.5 ) , so inteaccatrac variable will be rejected (eliminated)
print(z$loadings,digits = 3,cutoff = 0.7)
scree(EFA1)
fa.parallel(EFA1,fa="fa")
load <- z$loadings[,1:2]
plot(load,type = "n")
text(load, labels = names(EFA1),cex = .7)
library(psych)
loads <- z$loadings
fa.diagram(loads)
