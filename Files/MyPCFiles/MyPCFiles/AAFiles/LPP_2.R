# LPP Using R
# MAX Z = 6X – 3Y
# s.t.	2X + 2Y < 20
# 6X > 12
# 4Y > 4
# 4X + Y < 20
# where:  X, Y > 0, where x and y are integers

obj.fun<-c(6,-3)
constr<-matrix(c(2,2,6,0,0,4,4,1),ncol=2,byrow=TRUE)
constr.dir<-c("<=",">=",">=","<=")
rhs<-c(20,12,4,20)
library(lpSolve)
sol<-lp("max",obj.fun,constr,constr.dir,rhs,compute.sens = TRUE)
sol
sol$solution 







