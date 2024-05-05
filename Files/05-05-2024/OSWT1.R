# Wilcoxon One Sample Test
# it is a non-parametric option of one sample T-test
OSWT1 <- read_excel("D:/Dhruva/OSWT1.xlsx")
attach(OSWT1)
wilcox.test(diameter, mu = 25, alternative = "two.sided")
# just indication: (does not mean it is accepted, need to check p-value)  
# alternative hypothesis: true location is not equal to 25
# Mann Whitney U test
# it is a non-parametric option of independent sample T-test
MW1 <- read_excel("D:/Dhruva/MW1.xlsx")
attach(MW1)
str(MW1)
MW1$Store<-as.factor(MW1$Store)
str(MW1)
wilcox.test(Sales ~ Store, data=MW1)
# there is no significant difference in the sales of two stores
# Since the p-value = 0.3427 which is > 0.05 so the null hypothesis is accepted so there is no significant difference in the sales of two stores  
# if bigger null accepted
# if small alternate accepted
# if two types of ranking is there then use mann whitney (difference)
# comparison is done on the basis of median value
# t-test comparion on the basis of mean value
# Mtcars
data("mtcars")
attach(mtcars)
View(mtcars)
# 1-automatic 0-manual
wilcox.test(mpg ~ am, data=mtcars)
# there is a difference in milege in automatic vs manual
# Wilcoxon before and after 
# Wilcoxon signed Rank Test - Paired t-test
W1 <- read_excel("D:/Dhruva/W1.xlsx")
attach(W1)
wilcox.test(Before, After, paired = TRUE, alternative = "two.sided")
# Conclusion: since the p-value = 0.7728 which is > than 0.05 so the null hypothesis is accepted and alternative hypothesis is rejected it means that there is no significant difference in terms of Sales before and after the advertisement









