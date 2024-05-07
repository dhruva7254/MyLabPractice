# LPP Using R
# max Z = 5x+7y
# 5x <= 30
# 3y <= 18
# x,y>=0
# Solution of LPP
obj.fun<-c(5,7)
constr<-matrix(c(5,0,0,3),ncol=2,byrow=TRUE)
constr.dir<-c("<=","<=")
rhs<-c(30,18)
library(lpSolve)
sol<-lp("max",obj.fun,constr,constr.dir,rhs,compute.sens = TRUE)
sol
sol$solution 






