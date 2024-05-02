# Paired T-tests
pair_t <- read_excel("D:/Dhruva/pair_t.xlsx")
attach(pair_t)
# Assumptions
# Normality
shapiro.test(Diff)
# Paired T-test
t.test(Bef,Aft,mu=0,paired = T)
mean(Aft)
mean(Bef)
mean(Bef)-mean(Aft)
