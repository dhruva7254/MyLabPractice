# Exploratory Factor Analysis
EFA1 <- read_excel("D:/Dhruva/EFA1.xlsx")
attach(EFA1)
str(EFA1)
library(psych)
KMO(EFA1)
r1=cor(EFA1)
r1
pca(r1,nfactors = 10,rotate = F)
z = pca(r1, nfactors = 3,method = regression, rotate = "varimax", scores = T)
z
z$values
print(z$values,digits=3)
cortest.bartlett(EFA1)

# OR
library(REdaS)
KMOS(EFA1)
r=cor(EFA1)



