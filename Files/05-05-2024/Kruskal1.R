# Kruskal Wallis H test
# it is a non-parametric option of Annova (one-way)
data("iris")
View(iris)
attach(iris)
kruskal.test(Petal.Length ~ Species, data = iris)
# Hypothesis
# Null Hypothesis H0: There is no significant difference in the petal length of the 3 species(setosa,versicolor,virginica) 
# Alternative Hypothesis H1: There is significant difference in the petal length of the 3 species(setosa,versicolor,virginica)  
# Conclusion: since the p value is 0.000 which is < 0.05 so null hypothesis is rejected & alternative hypothesis is accepted so there is significant difference in the petal length of the 3 species   




