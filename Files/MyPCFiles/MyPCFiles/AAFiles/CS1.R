# Chi-Square Test
CS1 <- read_excel("D:/Dhruva/CS1.xlsx")
attach(CS1)
table(code)
table(grade)
table(code,grade)
TAB=table(code,grade)
TAB
# Chi-Square Test
chisq.test(TAB,correct=T) # given by Pearson
# X-squared = 13.571 is the output of the Chi-Square Formula
# Conclution: Since the p-value = 0.09364 which is greater than 0.05 so the Null hypothesis is accepted it means that there is no relation ship between educational background and academic grades
# table vale of chi square at 5% level of significance and degree of freedom 8 = 15.507
# the calculated value is less than table value - null hypothesis accepted
# df=(r-1)(c-1)=(5-1)(3-1)=8
CHI<-chisq.test(TAB,correct=T)
CHI$expected
# if not able to satisfy the condition 80% > 5
# then we go for fisher test
# Fisher test
fisher.test(TAB,conf.int = T,conf.level = 0.95)
# if there is a problem there is a solution in statistics

# Wilcoxon One Sample Test
# it is a non-parametric option of one sample T-test







